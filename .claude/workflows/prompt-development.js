export const meta = {
  name: 'prompt-development',
  description: 'Writer → Reviewer → Evaluator gate for player prompts: drafts vN, reviews independently, records verdicts, promotes approved drafts to current.md',
  whenToUse: 'Every time a player prompt is created or changed (mode "develop"), or to audit the deployed prompts (mode "review"). Args: {mode, brief, positions?, date}.',
  phases: [
    { title: 'Write', detail: 'prompt-writer drafts prompts/<pos>/vN.md' },
    { title: 'Review', detail: 'prompt-reviewer checks each prompt against the spec' },
    { title: 'Evaluate', detail: 'prompt-evaluator checks team coherence' },
    { title: 'Record', detail: 'write review records; promote approved drafts' },
  ],
}

// args: {
//   mode: 'develop' | 'review'   — develop = write + review + evaluate; review = audit current.md only
//   brief: string                — develop only: what to change and why (coach's words, match refs)
//   positions?: string[]         — subset of gk, def, mid, fwd1, fwd2 (develop: scope hint; review: files to audit)
//   date: 'YYYY-MM-DD'           — stamped into review records (scripts cannot read the clock)
//   prepassed?: string[]         — develop only: positions whose drafts passed review in an earlier run and are
//                                  unchanged; they skip the round-1 review and go straight to the Evaluator
// }

const ALL = ['gk', 'def', 'mid', 'fwd1', 'fwd2']
const LABEL = { gk: 'GK', def: 'DEF', mid: 'MID', fwd1: 'FWD1', fwd2: 'FWD2' }
const MAX_ITERATIONS = 3

const input = args || {}
const mode = input.mode === 'review' ? 'review' : 'develop'
const brief = input.brief || ''
const date = input.date || 'undated'
const prepassed = Array.isArray(input.prepassed) ? input.prepassed.filter(p => ALL.includes(p)) : []
const scope = Array.isArray(input.positions) && input.positions.length
  ? input.positions.filter(p => ALL.includes(p))
  : null
if (mode === 'develop' && !brief) throw new Error('develop mode needs args.brief: what to change and why')

const POSITION = { type: 'string', enum: ALL }

const WRITER_SCHEMA = {
  type: 'object',
  properties: {
    drafts: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          position: POSITION,
          version: { type: 'integer' },
          file: { type: 'string' },
          chars: { type: 'integer' },
          changed: { type: 'boolean', description: 'true if you modified this file in this round' },
        },
        required: ['position', 'version', 'file', 'changed'],
      },
    },
    summary: { type: 'string' },
  },
  required: ['drafts', 'summary'],
}

const REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    reviews: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          position: POSITION,
          version: { type: 'integer' },
          verdict: { type: 'string', enum: ['PASS', 'FAIL'] },
          failed_checks: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                check: { type: 'string' },
                severity: { type: 'string', enum: ['blocking', 'minor'] },
                quote: { type: 'string' },
                fix: { type: 'string' },
              },
              required: ['check', 'severity', 'fix'],
            },
          },
          notes: { type: 'string' },
        },
        required: ['position', 'version', 'verdict', 'failed_checks'],
      },
    },
  },
  required: ['reviews'],
}

const EVAL_SCHEMA = {
  type: 'object',
  properties: {
    verdict: { type: 'string', enum: ['APPROVE', 'REJECT'] },
    issues: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          positions: { type: 'array', items: POSITION },
          check: { type: 'string' },
          problem: { type: 'string' },
          fix: { type: 'string' },
        },
        required: ['check', 'problem', 'fix'],
      },
    },
    notes: { type: 'string' },
  },
  required: ['verdict', 'issues'],
}

const RECORD_SCHEMA = {
  type: 'object',
  properties: {
    written: { type: 'array', items: { type: 'string' } },
    promoted: { type: 'array', items: { type: 'string' } },
    script_output: { type: 'string' },
  },
  required: ['written', 'promoted'],
}

// Use the project's custom agent type; if it is not registered in this session, fall back to
// a default agent that reads the same role file (tool limits then rely on the instructions).
// Role agents run at 'high' effort: thorough enough for prompt review without the token cost of the session's top effort.
async function runRole(role, prompt, baseOpts) {
  const opts = { effort: 'high', ...baseOpts }
  try {
    const result = await agent(prompt, { ...opts, agentType: role })
    if (result) return result
    log(`${role}: no result from the custom agent type, retrying with the role file`)
  } catch (e) {
    log(`${role}: custom agent type unavailable (${e && e.message ? e.message : e}), using the role file`)
  }
  return agent(`Read .claude/agents/${role}.md and follow it as your role instructions (ignore its frontmatter).\n\n${prompt}`, opts)
}

function teamListing(drafts) {
  return ALL.map(p => {
    const d = drafts.find(x => x.position === p)
    return d ? `- ${LABEL[p]}: ${d.file} (NEW draft v${d.version})` : `- ${LABEL[p]}: prompts/${p}/current.md (unchanged)`
  }).join('\n')
}

// A draft fails only on blocking findings; minor ones are fixed when they cost no pasted characters.
function normalize(review) {
  const blocking = review.failed_checks.filter(c => c.severity !== 'minor')
  return { ...review, verdict: blocking.length ? 'FAIL' : 'PASS' }
}

function reviewFeedback(reviews, missing) {
  const lines = []
  for (const r of reviews) {
    lines.push(`Reviewer ${r.verdict} — ${LABEL[r.position]} v${r.version}:`)
    for (const c of r.failed_checks) {
      const tag = c.severity === 'minor' ? 'minor, fix only if it costs no pasted characters' : 'BLOCKING'
      lines.push(`- (${tag}) [${c.check}] ${c.quote ? `"${c.quote}" ` : ''}→ ${c.fix}`)
    }
  }
  for (const d of missing) lines.push(`Reviewer did not review ${d.file}; make sure it exists and follows the schema.`)
  return lines.join('\n')
}

function evalFeedback(evaluation) {
  const lines = ['Evaluator REJECT:']
  for (const i of evaluation.issues) {
    lines.push(`- [${i.check}] ${(i.positions || []).map(p => LABEL[p]).join('/')}: ${i.problem} → ${i.fix}`)
  }
  return lines.join('\n')
}

function recordMarkdown(position, version, review, evaluation, outcome, history) {
  const lines = [
    `# Review — ${LABEL[position]} v${version}`,
    '',
    `Date: ${date}`,
    `Mode: ${mode}`,
    `Brief: ${brief || '(audit of deployed prompt)'}`,
    '',
    `Reviewer: ${review ? review.verdict : 'NOT RUN'}`,
    `Evaluator: ${evaluation ? evaluation.verdict : 'NOT RUN'}`,
    `Outcome: ${outcome}`,
    '',
    '## Reviewer findings',
  ]
  if (!review) lines.push('- Not reviewed.')
  else if (!review.failed_checks.length) lines.push('- All checks passed.')
  else review.failed_checks.forEach(c => lines.push(`- **[${c.severity || 'blocking'}] ${c.check}**: ${c.quote ? `"${c.quote}" — ` : ''}${c.fix}`))
  if (review && review.notes) lines.push('', `Notes: ${review.notes}`)
  lines.push('', '## Evaluator findings (team)')
  if (!evaluation) lines.push('- Not evaluated.')
  else if (!evaluation.issues.length) lines.push('- No blocking issues.')
  else evaluation.issues.forEach(i => lines.push(`- **${i.check}** (${(i.positions || []).map(p => LABEL[p]).join(', ') || 'team'}): ${i.problem} Fix: ${i.fix}`))
  if (evaluation && evaluation.notes) lines.push('', `Notes: ${evaluation.notes}`)
  lines.push('', '## Iterations')
  history.forEach(h => lines.push(`- ${h}`))
  return lines.join('\n') + '\n'
}

let drafts = []
let reviews = null
let evaluation = null
let approved = false
let writerSummary = ''
let feedback = ''
const history = []
const latest = {}   // position -> most recent review (normalized)

if (mode === 'develop') {
  for (let iteration = 1; iteration <= MAX_ITERATIONS; iteration++) {
    phase('Write')
    const writerPrompt = [
      `Mode: develop. Iteration ${iteration} of ${MAX_ITERATIONS}.`,
      `Brief from the coach: ${brief}`,
      scope
        ? `Positions in scope: ${scope.join(', ')}. Change other positions only if coordination requires it.`
        : 'Decide which positions need changes from the brief and the match logs.',
      drafts.length
        ? `Revise these drafts in place (keep their version numbers). Change only what the feedback requires; leave drafts that passed untouched unless coordination forces it: ${drafts.map(d => d.file).join(', ')}`
        : '',
      feedback ? `Feedback to address:\n${feedback}` : '',
      'Report every draft of this run, with changed=true only for files you modified in this round.',
    ].filter(Boolean).join('\n\n')
    const written = await runRole('prompt-writer', writerPrompt, { label: `writer #${iteration}`, phase: 'Write', schema: WRITER_SCHEMA })
    if (!written || !written.drafts.length) {
      history.push(`Iteration ${iteration}: Writer produced no drafts`)
      break
    }
    for (const d of written.drafts) {
      drafts = drafts.filter(x => x.position !== d.position).concat([d])
    }
    writerSummary = written.summary
    // Seed reviews carried over from an earlier run for unchanged drafts.
    if (iteration === 1) {
      for (const d of drafts) {
        if (prepassed.includes(d.position) && !d.changed) {
          latest[d.position] = { position: d.position, version: d.version, verdict: 'PASS', failed_checks: [], notes: 'Passed review in an earlier run of this release and unchanged since; carried forward.' }
        }
      }
    }
    // Re-review a draft if it was changed this round or has not passed yet.
    const toReview = drafts.filter(d => d.changed || !latest[d.position] || latest[d.position].verdict !== 'PASS')
    const carried = drafts.filter(d => !toReview.includes(d))
    log(`Iteration ${iteration}: reviewing ${toReview.map(d => LABEL[d.position]).join(', ') || 'none'}${carried.length ? `; carrying PASS for ${carried.map(d => LABEL[d.position]).join(', ')}` : ''}`)

    if (toReview.length) {
      phase('Review')
      const result = await runRole('prompt-reviewer', [
        'Review these draft prompts independently. Judge only the files; you have not seen the writer\'s reasoning.',
        toReview.map(d => {
          const prev = latest[d.position]
          const prevFindings = prev && prev.failed_checks.length
            ? `\n  Previously flagged (verify each is fixed): ${prev.failed_checks.map(c => `[${c.severity}] ${c.check}: ${c.fix}`).join(' | ')}`
            : ''
          return `- ${LABEL[d.position]}: ${d.file}${prevFindings}`
        }).join('\n'),
        iteration > 1
          ? 'This is a revision round. Verify the previously flagged items. Raise a NEW blocking finding only if the revision introduced it or it would clearly cause wrong play; put everything else under minor or notes.'
          : '',
        'Mark each finding blocking (wrong in-game behavior, a rule/constraint contradiction, over budget, or a logged weakness not addressed) or minor (wording, changelog completeness, style). Return one review per file listed.',
      ].filter(Boolean).join('\n\n'), { label: `reviewer #${iteration}`, phase: 'Review', schema: REVIEW_SCHEMA })
      if (!result) {
        history.push(`Iteration ${iteration}: Reviewer returned nothing`)
        break
      }
      for (const r of result.reviews) {
        if (toReview.some(d => d.position === r.position)) latest[r.position] = normalize(r)
      }
    }
    reviews = { reviews: Object.values(latest) }
    const failed = drafts.map(d => latest[d.position]).filter(r => r && r.verdict !== 'PASS')
    const missing = drafts.filter(d => !latest[d.position])
    if (failed.length || missing.length) {
      const minorOnly = drafts.map(d => latest[d.position]).filter(r => r && r.verdict === 'PASS' && r.failed_checks.length)
      feedback = reviewFeedback(failed.concat(minorOnly), missing)
      evaluation = null
      history.push(`Iteration ${iteration}: Reviewer FAIL (${failed.map(f => LABEL[f.position]).concat(missing.map(m => `${LABEL[m.position]} not reviewed`)).join(', ')})`)
      continue
    }

    phase('Evaluate')
    evaluation = await runRole('prompt-evaluator', [
      'Evaluate the coherence of this proposed team:',
      teamListing(drafts),
      `Coach's brief (intent): ${brief}`,
      'REJECT only for blocking team issues; put minor points in notes.',
    ].join('\n\n'), { label: `evaluator #${iteration}`, phase: 'Evaluate', schema: EVAL_SCHEMA })
    if (!evaluation) {
      history.push(`Iteration ${iteration}: Reviewer PASS, Evaluator returned nothing`)
      break
    }
    if (evaluation.verdict === 'APPROVE') {
      approved = true
      history.push(`Iteration ${iteration}: Reviewer PASS, Evaluator APPROVE`)
      break
    }
    feedback = evalFeedback(evaluation)
    history.push(`Iteration ${iteration}: Reviewer PASS, Evaluator REJECT (${evaluation.issues.length} issue(s))`)
  }
  if (!approved) log(`Not approved after ${history.length} iteration(s): escalate to the coach`)
} else {
  const targets = (scope || ALL).map(p => ({ position: p, file: `prompts/${p}/current.md` }))
  phase('Review')
  reviews = await runRole('prompt-reviewer', [
    'Audit these deployed prompts independently. Judge only the files.',
    targets.map(t => `- ${LABEL[t.position]}: ${t.file}`).join('\n'),
    'Report each prompt\'s version from its header. Return one review per file.',
  ].join('\n\n'), { label: 'reviewer (audit)', phase: 'Review', schema: REVIEW_SCHEMA })
  if (reviews) reviews = { reviews: reviews.reviews.map(normalize) }
  phase('Evaluate')
  evaluation = await runRole('prompt-evaluator', [
    'Audit the coherence of the deployed team:',
    teamListing([]),
  ].join('\n\n'), { label: 'evaluator (audit)', phase: 'Evaluate', schema: EVAL_SCHEMA })
  const allPass = !!reviews && targets.every(t => reviews.reviews.some(r => r.position === t.position && r.verdict === 'PASS'))
  approved = allPass && !!evaluation && evaluation.verdict === 'APPROVE'
  history.push(`Audit: Reviewer ${allPass ? 'PASS' : 'FAIL'}, Evaluator ${evaluation ? evaluation.verdict : 'NOT RUN'}`)
  drafts = targets.map(t => {
    const r = reviews && reviews.reviews.find(x => x.position === t.position)
    return { position: t.position, version: r ? r.version : 0, file: t.file }
  })
}

// Record: one review record per position under prompts/<pos>/reviews/vN.md (the commit gate reads these).
phase('Record')
const outcome = approved
  ? (mode === 'develop' ? 'APPROVED — promoted to current.md' : 'APPROVED — deployed prompt passes audit')
  : (mode === 'develop' ? 'NOT APPROVED — escalate to coach; current.md unchanged' : 'AUDIT FOUND ISSUES — see findings')
const files = drafts.filter(d => d.version > 0).map(d => {
  const review = reviews ? reviews.reviews.find(r => r.position === d.position) : null
  return { path: `prompts/${d.position}/reviews/v${d.version}.md`, content: recordMarkdown(d.position, d.version, review, evaluation, outcome, history) }
})
const promote = approved && mode === 'develop' ? drafts : []
const record = await agent([
  'You are the release clerk of the prompt-development workflow. Do exactly the following, nothing else. Do NOT run any git command (no git add, commit, tag or push), even though CLAUDE.md describes committing after approval: that is the main session\'s job, not yours.',
  '1. Write each file below with exactly the given content (create directories as needed; overwrite if present):',
  files.map(f => `=== FILE: ${f.path} ===\n${f.content}=== END FILE ===`).join('\n\n'),
  promote.length
    ? `2. Promote the approved drafts: ${promote.map(d => `cp ${d.file} prompts/${d.position}/current.md`).join(' && ')}`
    : '2. Promote nothing. Do not touch any current.md.',
  '3. Run `python3 scripts/build-paste-ready.py` then `python3 scripts/build-dashboard.py`, and report their output briefly.',
].join('\n\n'), { label: 'record & promote', phase: 'Record', schema: RECORD_SCHEMA, effort: 'low' })

return {
  mode,
  status: approved ? 'approved' : (mode === 'develop' ? 'not-approved' : 'audit-issues'),
  iterations: history,
  writer_summary: writerSummary,
  drafts,
  reviews: reviews ? reviews.reviews : null,
  evaluation,
  records: record,
}
