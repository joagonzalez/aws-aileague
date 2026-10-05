# Workflow: Deploy Checklist

## Pre-Deploy Validation

Run through this checklist before every deployment to the AWS platform.

### Prompt Readiness
- [ ] All modified prompts passed the Reviewer (Stage 2 of prompt-development)
- [ ] All modified prompts passed the Evaluator (Stage 3 of prompt-development)
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
- [ ] Tag created: `deploy-vN-YYYY-MM-DD`
- [ ] Tag logged in `tags.md`
- [ ] Commit messages reference match context where applicable

## Deploy Steps

1. Verify all checks above are green
2. Copy prompt content from each `prompts/<position>/current.md` into the AWS platform
3. Select model for each agent
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
