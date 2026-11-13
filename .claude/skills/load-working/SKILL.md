---
name: load-working
description: Start a work session on the CAP 3764 team project. Pulls the latest main, finds the user's assigned task in docs/TEAM_WORKFLOW.md, sets up the task branch, and does the task within scope. Use when the user says /load-working, "start my task", or "what should I work on".
---

# /load-working

Follow `AGENTS.md` at all times. Steps:

1. **Who is the user?** Run `git config user.name` and match it against the owners in
   `docs/TEAM_WORKFLOW.md` (Pablo, Jorlfran, Lilly, Helen). If it does not clearly match,
   ask which teammate they are. Do not guess.
2. **Sync safely.**
   - `git status --short`: if there are uncommitted changes, show them and ask before doing
     anything (do not stash, reset, or discard).
   - `git fetch origin --prune`, then update `main` with `git pull --ff-only origin main`
     (on `main`) or `git merge --ff-only origin/main` after checking out the branch.
     If it cannot fast-forward, stop and report; do not force anything.
3. **Read the task.** Open `docs/TEAM_WORKFLOW.md` and list that person's tasks: deliverable,
   branch, reviewer. Also check `git branch -r` and `gh pr list` (if available) to see which
   are already started or merged. Tell the user the task list and propose the next unfinished
   one; confirm if there is more than one candidate.
4. **Branch.** If `origin/<branch>` exists, check it out and pull; otherwise create the
   branch from the updated `main` using the exact name from the workflow doc.
5. **Environment check.** Confirm `conda run -n cap3764-risk python -c "import risk_data"`
   works. If the env is missing or stale, tell the user to run
   `conda env create -f environment-cap3764-final-project.yml` (or `conda env update ... --prune`)
   from the repo root. Check that `data/processed/cleaned_data.csv` exists; if not, tell them to
   run `python src/risk_data/collect.py` then `python src/risk_data/clean.py`.
6. **Do the task.** Plan briefly, then implement only the deliverable listed for the task.
   Commit small and often with conventional messages. Other people's files are read-only unless
   the task says otherwise. If the task depends on someone else's unmerged work, say so.
7. **Verify** before reporting done: notebooks run top to bottom, no stray files in
   `git status`, no data or secrets staged.
8. Finish by summarizing what was done and suggest running `/cap3764-handoff`.
   Do not push or open a PR here.
