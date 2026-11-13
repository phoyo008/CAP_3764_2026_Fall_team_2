---
name: cap3764-handoff
description: Wrap up a CAP 3764 work session so everything is ready for review. Verifies the work, commits, pushes the task branch, and prepares the pull request description and reviewer. Use when the user says cap3764-handoff, "I'm done", or "leave everything ready".
---

# cap3764-handoff

Invoke as `/cap3764-handoff` in Claude Code or `$cap3764-handoff` in Codex. Follow `AGENTS.md`.
Goal: a teammate can review the PR without asking questions.

1. **Confirm context.** `git branch --show-current` must be the task branch (never `main`).
   Find the matching row in `docs/TEAM_WORKFLOW.md` (owner, deliverable, reviewer).
2. **Verify honestly.**
   - Re-execute each notebook you changed from a clean kernel:
     `conda run -n cap3764-risk jupyter nbconvert --to notebook --execute --inplace <nb>`
     (only notebooks that belong to this task). Report any failure; do not hide it.
   - If code in `src/` changed: `conda run -n cap3764-risk python -m pytest tests -q`.
   - `git status`: no `Untitled*.ipynb`, data, `.pptx`, caches, or credentials staged.
   - Check the deliverable against the task row and any brief in `docs/MODELING_NOTES.md`.
   - Check that every number written in markdown matches the executed output.
3. **Docs.** Update README sections or the checklist only if this task changes them. New
   dependencies must already be pinned in the env yml.
4. **Commit.** Clear conventional commits (`docs:`, `feat:`, ...), only this task's files, under
   the user's own git identity.
5. **Push** the branch with `git push -u origin <branch>` after telling the user what will be
   pushed. Never force-push.
6. **Prepare the PR.** Write the description and show it to the user:
   - **What**: summary of changes and which task row it closes
   - **Why**: the rubric item or feedback comment it addresses
   - **How to test**: exact commands (env, data, which notebook to run)
   - **Results**: key table or figure, copied from executed output only
   - **Open questions / known issues**
   - **Reviewer**: from the review rotation in the workflow doc
   Open it with `gh pr create` only after the user confirms.
7. **Leave a status line** for the team: task, branch, PR link, what is left, who reviews.
8. Remind the user to review their assigned PRs and to submit their peer-review form.
