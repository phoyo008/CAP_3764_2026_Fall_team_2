---
name: load-working
description: Start a work session on the CAP 3764 team project. Pulls the latest main, finds the user's assigned tasks in docs/TEAM_WORKFLOW.md, sets up the task branch, and does the task within scope. Use when the user says load-working, "start my task", or "what should I work on".
---

# load-working

Invoke as `/load-working` in Claude Code or `$load-working` in Codex. Follow `AGENTS.md` at all
times. Steps:

1. **Who is the user?** Run `git config user.name` and `git config user.email` and match
   against the owners in `docs/TEAM_WORKFLOW.md` (Pablo, Jorlfran, Lilly, Helen). Names in
   git may be GitHub handles (for example `phoyo008` is Pablo). If it is not clear, ask which
   teammate they are. Do not guess.
2. **Sync safely.**
   - `git status --short`: if there are uncommitted changes, show them and ask before doing
     anything (do not stash, reset, or discard).
   - `git fetch origin --prune`, then update `main` with `git pull --ff-only origin main`
     (on `main`) or `git merge --ff-only origin/main` after checking out your branch.
     If it cannot fast-forward, stop and report; do not force anything.
3. **Read the task.** Open `docs/TEAM_WORKFLOW.md` and list that person's tasks (deliverable,
   branch, reviewer). If the deliverable has a brief in `docs/MODELING_NOTES.md`, read it too.
   Check `git branch -r` and `gh pr list --state all` (if available) to see which tasks are
   started or merged. Show the list and propose the next unfinished one; confirm when more than
   one is possible.
4. **Dependencies.** If the task imports code from another task (for example the modeling
   module) that is not merged into `main` yet, say so and stop until it is.
5. **Branch.** If `origin/<branch>` exists, check it out and pull; otherwise create the branch
   from the updated `main` using the exact name in the workflow doc.
6. **Environment check.** Run `conda run -n cap3764-risk python -c "import risk_data"`. If the
   env is missing or stale, tell the user to run
   `conda env create -f environment-cap3764-final-project.yml` (or `conda env update -f ...`)
   from the repo root, and to register the kernel (see README). Check that
   `data/processed/cleaned_data.csv` exists; if not, tell them to run
   `python src/risk_data/collect.py` then `python src/risk_data/clean.py`.
7. **Do the task.** Plan briefly, then implement only the deliverable listed for the task, and
   write the interpretation from your own executed output. Commit small and often with
   conventional messages, under the user's own git identity. Other people's files are read-only
   unless the task says otherwise.
8. **Verify** before reporting done: notebooks run top to bottom from a clean kernel, tests pass
   if code in `src/` changed, nothing stray in `git status`, no data or secrets staged.
9. Finish by summarizing what was done and suggest running `cap3764-handoff`.
   Do not push or open a PR here.
