# Execution environments and agent coordination

## Establish the working baseline

Distinguish the designated shared version from the checkout used for execution. Record the real repository and baseline according to the project's policy; do not import a reference project's GitHub account, default branch, shell, or local drive paths.

At a new task, environment switch, or resumed interrupted edit, inspect the repository root, remote, branch, commit, and worktree changes. Fetch the designated remote when network access and policy allow. Repeating fetch on every message during uninterrupted editing adds no useful assurance.

For a clean checkout on the designated branch, compare it with its remote counterpart. A fast-forward can update an exclusively behind checkout when the project permits it. Reread changed sources afterward.

Preserve dirty worktrees and local commits. Determine ownership before integrating. Do not automatically stash, reset, discard, or force-push. Continue the original task on its existing baseline when appropriate; use a separate worktree from the verified remote for unrelated work that must not mix with it.

If fetching fails, state the current branch and known commit without claiming synchronization. Continue safe reads. Follow the user's or project's offline-edit policy; network failure does not silently authorize divergent writes.

## Coordinate by ownership

A single active editor can use the project's normal checkout. Concurrent implementation agents need isolated worktrees or equivalent isolated copies and non-overlapping ownership. Read-only reviews can share sources; disposable evaluation projects can use isolated temporary directories.

Delegation is conditional on the task and available authorization, not a standing instruction to spawn agents. When used, give each agent the concrete outcome, source references, baseline, allowed files or systems, validation expectation, and limits on external actions. Give an independent evaluator raw inputs and a realistic request without the intended answer or suspected defect.

The coordinator integrates outcomes, checks conflicts and combined behavior, and updates shared handoff state. Subagent completion does not itself mean integration, acceptance, or release. Avoid several agents concurrently maintaining the same current-work file or remote document.

## Publish and hand off

Commit, push, merge, deployment, and external messages follow the user's authorization and project policy. Fetching does not grant publication permission. Once publication is authorized, finish the reviewable change and relevant tests, fetch again, integrate remote changes, and push normally. On rejection, inspect the difference instead of forcing it. Verify the remote's actual resulting commit.

Report where unsynchronized work remains. Git does not transport untracked or ignored assets, installed tools, credentials, or access rights. A successful local test does not establish a second environment's readiness.

Skill maintenance may involve a source repository, an installed copy, and distribution on the remote. Compare their commits and content before updating; preserve local improvements. State which copies were updated rather than calling all of them "latest" without verification.
