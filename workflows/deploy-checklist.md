# Workflow: Deploy Checklist

## Pre-Deploy Validation

Run through this checklist before every deployment to the AWS platform.

### Prompt Readiness
- [ ] All modified prompts passed the Reviewer (Stage 2 of prompt-development)
- [ ] All modified prompts passed the Evaluator (Stage 3 of prompt-development)
- [ ] Each changed position has `prompts/<pos>/reviews/vN.md` with `Reviewer: PASS` and `Evaluator: APPROVE` (the commit hook enforces this)
- [ ] Each modified prompt's `current.md` is updated with the approved version
- [ ] Version numbers are incremented correctly

### Team Coherence
- [ ] All 5 `current.md` files are present and non-empty
- [ ] Coordination sections are bidirectionally consistent
- [ ] Formation in prompts matches `strategy/formation.md`

### Match Log Integration
- [ ] If this deploy follows a match, the match debrief is complete
- [ ] Action items from the debrief are addressed in the new prompts
- [ ] No regressions: effective rules from previous versions are preserved

### Git Hygiene
- [ ] All changes committed with descriptive messages
- [ ] Annotated tag created on the release commit: `deploy-vN-YYYY-MM-DD`
- [ ] Tag logged in `tags.md` (update "Played in" after each match)
- [ ] Pushed with `git push origin master --follow-tags`
- [ ] Commit messages reference match context where applicable

## Deploy Steps

1. Verify all checks above are green
2. Run `python3 scripts/build-paste-ready.py` (fails on missing sections or >6000 chars; review any warnings), then copy each player's code block from `deploy/paste-ready.md` into the AWS platform
3. Make sure `deploy/platform-state.json` matches what you are about to deploy (prompt per player, model per player), then regenerate `deploy/paste-ready.md`.
4. Select the model for each agent, and check every dropdown against the `Model:` line in its prompt header (match 002 ran MID on the wrong model)
4. Click "Deploy changes" (first time) or "Redeploy changes" (updates)
5. Verify deployment succeeded on the platform

## Post-Deploy

- [ ] Run a practice match if possible before competitive play
- [ ] Note the deployed versions in the next match log entry

## Rollback

If a deployment performs poorly:
1. Identify which position(s) regressed (via match debrief)
2. Check `tags.md` for the last known good tag
3. `git checkout <tag> -- prompts/<position>/current.md` for the affected position
4. Re-deploy with the rolled-back prompt
5. Log the rollback in `tags.md`
