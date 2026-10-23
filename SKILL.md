---
name: bootstrap-project-os
description: Establish or refactor project collaboration rules, source ownership, cold starts, and document maintenance. Use to make a repository agent-ready, connect existing project sources, or simplify a Project OS with duplicated context, changelogs, decision logs, or archives. Not for ordinary feature work or routine status updates.
---

# Bootstrap Project OS

Make a project resumable by a collaborator who has no chat history. They must be able to find the current goal, the source that owns a fact, the next action, and the boundary of their authority. Minimize the work required to keep those answers correct.

## Choose the scope

- **Bootstrap** establishes missing collaboration and source routes.
- **Onboard** grounds missing project facts using existing sources or user answers.
- **Audit** reports material problems without writing files.
- **Repair** updates an existing system, including migration from an older Project OS.

Follow explicit discussion-only requests without writing. A repair request authorizes the necessary edits within its scope; do not ask again for routine edits already authorized. Ask only when a material authority choice, uncertain disposal, or external action is not covered.

Read [governance-model.md](references/governance-model.md) for a bootstrap or structural repair. Then load only the applicable branch:

- Existing changelogs, decision logs, archives, or overloaded entries: [migration.md](references/migration.md).
- Missing identity, current goal, or source authority: [onboarding-protocol.md](references/onboarding-protocol.md).
- Directory or asset changes: [asset-placement.md](references/asset-placement.md).
- Multiple execution environments, Git synchronization, or concurrent agents: [collaboration.md](references/collaboration.md).
- Broad validation or skill testing: [validation-rubric.md](references/validation-rubric.md).

## Inspect and establish the baseline

Read the target's existing agent rules completely. Confirm the repository root, current branch and changes, and the project's designated remote baseline. Follow its Git policy before editing; keep nested repositories and installed skills separate from the parent project.

Read the existing context and current-work entries, then their source index when locating facts. Use shallow discovery only when sources or boundaries are unknown:

```text
python <skill-dir>/scripts/inspect_project.py --root <project-root>
```

The inspector reads metadata only. Respect stricter project exclusions. Never open credential files; identify sensitive locations by path only. Do not recursively read media, generated material, archives, or independent repositories.

Distinguish confirmed facts, proposals, observations, and unknowns. A task checklist cannot define the whole project without explicit authority. Source scope determines what it can establish: requirements describe intended behavior, code describes implementation, runtime evidence describes the observed environment. Preserve material disagreement instead of choosing whichever source is newest or longest.

Before writing, briefly state the sources to reuse, the concrete defects to fix, and any unresolved choice that actually affects the result. Use the project's language, facts, tools, and existing coherent layout.

## Build or repair the routes

Four responsibilities normally suffice. Reuse equivalent existing sources rather than forcing these names or creating duplicates:

| Responsibility | Default owner | Update when |
|---|---|---|
| Collaboration rules | `AGENTS.md` | Cross-task operating rules change |
| Stable context | `project_context.md` | Project identity, scope, or stable principles change |
| Current handoff | `current_work.md` | The current goal, blocker, or next action changes |
| Source navigation | `artifact_index.md` | A source, its ownership, or its location changes |

Cold start normally reads `AGENTS.md`, then stable context and current work. Read the index to locate task-specific sources. History and unrelated domains stay out of that route.

Maintain each conclusion in its responsible source, with the rationale, scope, exceptions, and evidence needed to act on it. Restructure that source into a coherent current account; remove or qualify obsolete passages within the affected scope. Do not append each conversation as another layer of instructions.

Version history records edits. A general changelog or independent decision ledger is not part of the default kernel. Preserve an existing ADR, release note, or audit record when it has a distinct reader or operational purpose. Read the migration reference before retiring any such file; never discard its unique rationale or uncommitted content.

Keep business detail in its domain source, execution detail in its tracker, reusable methods in a runbook, and executable behavior in tools. A normal change updates its owner and only the entry routes affected by that change. A proposed plan, document delivery, acceptance, and production release remain separate states.

Use [templates](assets/templates/) only for missing owners. Remove unused sections and replace placeholders with grounded facts or explicit unknowns. Machine markers are optional; never add administrative text merely to satisfy a validator.

## Verify the result

For a focused repair, reread the changed source and relevant current references, then inspect the diff. For structural changes, also run:

```text
python <skill-dir>/scripts/validate_project_os.py --root <project-root> --json
```

This checks readable role owners, route registration, placeholders, and path safety. It reports `valid` or `invalid`, always with `semantic_status: not_checked`. It does not establish factual accuracy, source freshness, or successful collaboration.

Use the cold-start and update scenarios in the validation rubric. Fix defects that cause wrong conclusions, lost information, broken handoffs, conflicting ownership, or unsafe actions. Do not expand the task to enforce preferred headings, file counts, wording, or speculative edge cases. Stop when the authorized outcome works and no material defect remains.

Report the result, tests actually performed, material unknowns, and the next usable entry. State whether changes are local, committed, or verified on the designated remote. Never imply a skill is installed on another device or an external project is migrated merely because this repository was updated.
