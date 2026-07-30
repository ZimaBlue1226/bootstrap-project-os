---
name: bootstrap-project-os
description: Bootstrap, onboard, audit, or repair a durable local project-governance system. Establish source authority, project context, current-work tracking, decision history, artifact and directory placement, change history, cold-start instructions, lifecycle update routing, and large-asset or sensitive-file safeguards. Use when a user asks to initialize project management in a repository, make a project agent-ready, preserve lifecycle context for handoffs, connect existing GitHub repositories, documents, websites, or trackers as project sources, define where new requirements and project assets should live, or untangle overloaded and conflicting project documents. Do not use for ordinary feature work or routine status updates unless the user explicitly asks to establish or repair the governance system.
---

# Bootstrap Project OS

## Objective

Install an authority, lifecycle, and placement-routing system for future collaborators. Treat generated files as the control surface, not the goal.

Preserve the project's own facts, tools, roles, language, and working style. Never use the largest, only, or most detailed document as a proxy for the whole project without confirming its scope and authority.

## Required references

Read these files before acting:

1. `references/governance-model.md` for semantic roles, lifecycle routing, and the promotion firewall.
2. `references/project-adaptation.md` before inspecting or mapping an existing project.
3. `references/onboarding-protocol.md` before asking for core facts or user-provided sources.
4. `references/asset-placement.md` before proposing directories, moving existing assets, or defining where future assets belong.
5. `references/validation-rubric.md` before final validation.

Use `assets/templates/` as structural aids. Adapt them to the target project and remove every placeholder before delivery.

## Operating boundaries

- Derive project facts only from the target project, accessible sources supplied by the user, and user confirmations.
- Separate evidence status, source scope, authority, and time horizon.
- Never promote an inference, proposal, task detail, discussion, archived statement, or ordinary webpage claim into confirmed project-level truth.
- Treat Checklist, Task, Todo, Issue, plan, launch guide, migration note, and other work-item documents as task-scoped until the user or an explicit project-level source says otherwise.
- Keep `AGENTS.md` free of business workflow details. It may contain cross-task collaboration rules and project-wide operational safeguards, not task stages, checklist IDs, feature rules, or domain plans.
- Inspect shallowly first. Do not recursively read source trees, media collections, datasets, model files, dependency directories, build outputs, or archives.
- Treat archive contents as non-authoritative and exclude them from ordinary discovery. Read only the archive boundary unless a history task explicitly requires archived material.
- Identify potential credentials by path and filename only. Never open credential or secret files.
- Read existing `AGENTS.md` and equivalent governance documents completely before proposing changes.
- Preserve existing files and user changes. Do not overwrite, rename, move, delete, or archive material without explicit authorization.
- Do not change code, Git configuration, issue trackers, remote systems, permissions, or deployment settings unless separately requested.
- Reuse an existing canonical source when its role is clear. Do not create a duplicate source merely to match default filenames.
- Use the user's requested language. If unspecified, use the language of the request and existing project documentation.

## Workflow

### 1. Resolve the target and intent

Confirm the project root. Distinguish:

- **Bootstrap**: install governance where it is absent or minimal.
- **Onboard**: connect project identity, sources, boundaries, and current work to an installed governance kernel.
- **Audit**: report gaps and conflicts without modifying files.
- **Repair**: correct an existing system while preserving project facts.

If the user requests only discussion, planning, or audit, do not write files.

### 2. Inspect safely

Run:

```text
python <skill-dir>/scripts/inspect_project.py --root <project-root>
```

Use the report to locate likely governance documents, technology markers, external-tool pointers, existing placement directories, root-level document candidates, archive boundaries, large-asset candidates, and sensitive-file candidates. The script does not read file contents.

Then read only relevant text entry points:

- Existing agent instructions and repository rules
- Project overview or README
- Roadmap, status, decision, architecture, requirements, and artifact indexes
- Documents explicitly referenced by those entry points

Follow existing project-specific safety rules before continuing.

### 3. Run concise, source-aware onboarding

Before writing a bootstrap when core project facts or source scope are unclear, ask one compact onboarding prompt. Invite either direct answers or existing sources such as:

- GitHub or other repositories
- README, product briefs, architecture or requirements documents
- Connected documents in Feishu/Lark, Notion, Google Drive, SharePoint, or similar systems
- Public websites, product pages, or help centers
- Jira, Linear, GitHub Issues, Base, spreadsheets, or other trackers
- Design, QA, deployment, or operational systems

Ask in plain language:

1. What is the project, and for whom does it exist?
2. What stage is the whole project in, and what project-level outcome matters next?
3. Which discovered or supplied sources describe the whole project, and which describe only one task, checklist, module, or reference?
4. Where do code, work status, and external runtime truth live, and what sensitive or approval boundaries apply?

Do not ask again for facts already explicit in the user's request or a confirmed project-level source. If a source is inaccessible, ask the user to connect it, export it, provide a local path, or summarize the necessary facts.

Read only the necessary source entry points. A public website is evidence or runtime surface, not automatically a canonical internal source.

Reflect a short intake summary before changing authority:

```text
Project:
Project-level stage and immediate outcome:
Project-level sources:
Work-item or reference sources:
Operating and sensitive boundaries:
Existing or proposed asset-placement policy:
Still unknown:
```

Ask for confirmation only when a proposed classification or promotion would materially change project-level truth. If the user explicitly prefers a kernel-only install, proceed with unknowns and mark the result `READY_WITH_GAPS`.

### 4. Classify sources and apply the promotion firewall

For each relevant source or candidate fact, classify:

- **Scope**: project, domain/module, workstream, task/checklist, reference/archive, or unknown.
- **Authority**: user-confirmed, explicitly designated canonical, source-declared, external runtime, ordinary evidence, inferred, proposed, or disputed.
- **Time horizon**: stable context, current project work, execution detail, durable decision, or history.

Promote a fact only when its destination requirements are met:

```text
project_context.md = project scope + confirmed authority + stable fact
current_work.md     = project scope + confirmed authority + current project state
decision_log.md     = project scope + explicit confirmation + durable choice
AGENTS.md           = cross-task collaboration rule or project-wide operational safeguard
```

Everything else stays in its domain or task source, is indexed with a boundary, or remains an explicit unknown. When scope or authority is ambiguous enough to change the result, pause and ask.

### 5. Establish the asset-placement policy

Read `references/asset-placement.md`.

Prefer an existing coherent project structure. When no clear convention exists, propose the minimal standard baseline and create directories only when the first real asset needs them.

For each relevant existing asset, recommend one disposition:

```text
keep
relocate
archive
externalize
needs-confirmation
```

Reserve the project root for governance entry points, confirmed project-level anchors, and files required there by the toolchain. Do not leave ordinary requirements, task checklists, research notes, background material, or generated reports at the root without an explicit reason.

Preview all proposed moves with old path, new path, classification, link updates, and authority effect. Existing assets may move only after user authorization.

Ask the user to confirm the placement policy once. After confirmation:

- Record concise future-asset rules in `AGENTS.md`.
- Record the detailed directory map and lifecycle in `artifact_index.md`.
- Place newly created assets automatically when classification is unambiguous.
- Ask only when an asset spans multiple domains, would replace authority, or requires moving existing material.
- Update links, source maps, and changelog whenever an asset is relocated or archived.

Do not copy external canonical sources locally merely to fit the directory structure.

### 6. Build the role map

Map the semantic roles in `references/governance-model.md` to existing sources. Prefer existing valid sources. Use these defaults only for missing roles:

```text
AGENTS.md
project_context.md
current_work.md
decision_log.md
artifact_index.md
changelog.md
archive/README.md
```

For every non-governance source, record what it owns and what it must not determine. Keep code, product, technical, legal, design, research, QA, operational, external-system, and execution sources at their actual locations.

### 7. Preview material changes

Before modifying an established project, summarize:

- Existing sources to reuse and their proposed scope
- Missing files to create
- Existing files needing targeted edits
- Conflicts or duplicated facts
- Proposed project-level promotions
- Proposed asset dispositions and the recommended directory baseline
- Items requiring user confirmation

Proceed without another confirmation when the user already authorized implementation and no material source-authority decision remains. Ask before overwriting, moving, renaming, deleting, archiving, or changing source authority.

### 8. Generate or repair the system

Ensure:

- `AGENTS.md` contains only cross-task rules, cold-start order, update routing, uncertainty handling, safety boundaries, and the confirmed future-asset placement policy.
- `project_context.md` contains stable confirmed project-level truth and a grounding-status marker.
- `current_work.md` contains project-level progress, milestones, blockers, decisions needed, and handoff; task-level execution stays in its own source.
- `decision_log.md` contains only confirmed project-level durable choices with provenance.
- `artifact_index.md` maps scope, ownership, non-ownership, authority, lifecycle, directory purpose, external sources, large assets, and sensitive boundaries.
- `changelog.md` records effective substantive changes in reverse chronological order.
- `archive/README.md`, when an archive is used, marks it non-authoritative.

Populate documents with real known facts. Do not leave unresolved placeholders or present example records as real.

Set the grounding marker in `project_context.md`:

```text
<!-- project-os:grounding-status=ready -->
```

Use `needs-input` instead of `ready` when project purpose, project stage, immediate project objective, or source authority remains materially incomplete.

### 9. Validate

Run:

```text
python <skill-dir>/scripts/validate_project_os.py --root <project-root>
```

Interpret:

- `READY`: structure is valid, core project facts are grounded, and cold start is usable.
- `READY_WITH_GAPS`: governance is structurally usable, but onboarding facts or authority mappings still need user input.
- `INVALID`: structural, safety, placeholder, or authority-boundary errors remain.

Fix all errors and review warnings. Then perform the manual cold-start and contamination checks in `references/validation-rubric.md`.

### 10. Report and onboard the user

Report:

- Files created or changed
- Existing sources reused and how they were classified
- Assets kept, relocated, archived, or externalized
- Confirmed placement policy for future assets
- Validation state
- Remaining project-specific unknowns
- Exact cold-start sequence
- One concrete next-best source or fact to provide

Explain how to resume incomplete onboarding. Do not describe suggestions, task-level plans, or external evidence as confirmed project decisions.

## Completion standard

Installation is complete only at `READY`: governance roles are unambiguous, core project facts are grounded, each source has a clear scope, authority, lifecycle, and placement boundary, cold start works, future assets have a unique destination, task details do not pollute project-level governance, and no sensitive content was read or copied.

At `READY_WITH_GAPS`, explicitly say that the kernel is installed but project onboarding is incomplete; never claim full completion.
