# bootstrap-project-os

[中文](README.zh.md) | [English](README.md)

A Codex skill for making projects resumable across agents and environments, and for simplifying existing project governance.

A collaborator should be able to recover the current goal, find the responsible source, and act within the right boundaries without replaying chat history. The skill builds those routes while keeping maintenance proportional to the project.

## The model

| Responsibility | Default owner | What belongs there |
|---|---|---|
| Collaboration | `AGENTS.md` | Reading order, operating boundaries, coordination, update routing |
| Stable context | `project_context.md` | Purpose, scope, stable principles and system boundaries |
| Current handoff | `current_work.md` | The current goal, blockers and next useful action |
| Navigation | `artifact_index.md` | Responsible sources, access boundaries, asset locations |

These are responsibilities, not four mandatory new files. Reuse existing README, status, index, or external owners. Normal cold start reads the rules, context, and handoff, then uses the index for the relevant domain.

Decisions and useful rationale stay with the rule they explain. Git or document-system history records changes. General changelogs, independent decision ledgers, archive copies, and migration inventories are not default outputs. Existing ADRs, user-facing release notes, and audit records remain when they have a distinct purpose.

Requirements, design, code, execution tracking, and observed runtime state answer different questions. Their authority is scoped; a newer runtime observation does not silently rewrite a requirement.

## Use

```text
Use $bootstrap-project-os to establish a project collaboration system using the sources already here.
```

```text
Use $bootstrap-project-os to audit this project. Report material problems without changing files.
```

```text
Use $bootstrap-project-os to refactor this older installation. Preserve useful facts and rationale, remove redundant maintenance, and verify cold start and update routing.
```

Bootstrap creates missing routes. Onboard grounds missing facts. Audit is read-only. Repair changes an established system within the requested scope.

A repair reads existing owners before writing. It restructures their current account, reconciles affected references, and retires redundant material only after checking consumers, unique information, authorization, and historical recovery. It does not apply another project's product rules, local paths, or release policy.

## Installation and updates

This private repository requires GitHub access. Its root is the skill package. For the established personal skill layout:

```bash
git clone https://github.com/ZimaBlue1226/bootstrap-project-os.git ~/.codex/skills/bootstrap-project-os
```

If the skill is already installed, inspect its remote, branch, local commits, and changes first. A clean checkout with no local commits can fetch and fast-forward the designated remote branch. Preserve and reconcile local improvements before updating a divergent installation.

Updating this skill does not migrate another project automatically. Invoke Repair in that project after obtaining the updated skill. [The migration guide](references/migration.md) explains how to preserve useful legacy content.

## Inspection and validation

Python 3.12 or later; standard library only.

```bash
python scripts/inspect_project.py --root <project-root>
python scripts/validate_project_os.py --root <project-root> --json
python -B -m unittest discover -s scripts/tests -v
```

The inspector reads metadata, skips sensitive and large-asset areas, and respects links and nested-repository boundaries. Use the target project's stricter exclusions when needed.

The validator reads role owners without changing files. It reports `status: valid|invalid`, `structure_status: pass|fail`, and `semantic_status: not_checked`. Exit code is 0 for structurally valid, 1 for invalid, and 2 for invalid CLI input or an unusable root. External owners are registered without fetching them.

This structural status replaces the previous automated `ready|ready_with_gaps|invalid` contract. A reviewed handoff may still use `READY`, `READY_WITH_GAPS`, or `INVALID`, based on actual source and cold-start checks. Missing legacy markers and optional logs are not defects.

Alternative role owners use an optional mapping in AGENTS. Explicit legacy mappings for purposeful decision or history sources remain supported. See [validation](references/validation-rubric.md) for the schema and behavioral checks.

In a restricted environment, set the process's standard `TMP` and `TEMP` to a writable scratch directory before running tests. The tests create and clean isolated synthetic projects there.

## Package maintenance

`SKILL.md` is the agent entry. References contain conditional procedures; four templates help create missing owners; scripts implement deterministic checks. The two READMEs describe the package for people.

For material changes, run script regressions and realistic isolated trials on both a new project and an established one. Review actual decisions and artifacts, including preservation of useful rationale and untouched unrelated files. Do not treat phrase matching or a structural pass as behavioral evidence.

Keep repository source, installed copies, and the remote distinct. Publish only with authorization, verify the resulting remote commit, and state which copies were updated.
