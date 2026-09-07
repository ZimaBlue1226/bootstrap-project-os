# Project OS validation rubric

## Contents

1. Structural checks
2. Grounding checks
3. Contamination checks
4. Placement checks
5. Semantic checks
6. Operational checks
7. Cold-start test
8. Result states
9. Severity

## Structural checks

The script checks file presence, declarations, basic reference registration, placeholders, and placement signals. Its `status` is NOT a semantic verdict: JSON always reports `semantic_status: not_checked`. A `ready` marker is a project declaration, not an independently verified fact. Keep the automated result and manual review outcome separate in the handoff.

### Reusing role owners

Default filenames work without extra configuration. When a role already has a confirmed owner, declare only the overrides in one JSON comment in the local `AGENTS.md`; document its scope in the normal index as well. For example:

```text
<!-- project-os:role-map={"stable_context":"README.md","durable_decisions":"docs/adr-index.md"} -->
```

Supported keys are `collaboration_rules`, `stable_context`, `current_work`, `durable_decisions`, `artifact_navigation`, and `effective_history`. `AGENTS.md` remains the local collaboration/safety entry; other roles can map to project-relative files or HTTPS/HTTP source URLs. Omitted keys retain default paths. Local paths cannot traverse links/junctions, escape the project, or enter sensitive, archived or VCS locations. Do not put credentials in mappings. Directories are not file owners: use an ADR index, not the ADR directory itself.

Shared files may own multiple roles when the sections and update boundaries are explicit; do not infer this from filenames. The grounding marker belongs in the mapped stable-context source; directory and scope markers belong in the mapped index. AGENTS must register the mapped source references, but registration alone does not prove a valid reading order. Verify the three-role default and conditional discovery manually. Mapped external owners are never fetched by the script and always produce automated `READY_WITH_GAPS`; separately report the manual access, scope and freshness review without changing that structural result. Do not create local competing copies just to silence it.

- Every selected semantic role has exactly one declared authority.
- The cold-start sequence points to real, readable files or explicit external sources.
- Existing equivalent paths are documented.
- Detailed canonical sources are indexed without being copied.
- Large assets and sensitive paths are identified without exposing their contents.
- Archive material is clearly marked non-authoritative.
- Generated files contain no unresolved template placeholders.
- Archive contents are excluded from ordinary source discovery.

## Grounding checks

- `project_context.md` contains exactly one grounding marker:

```text
<!-- project-os:grounding-status=ready -->
```

or:

```text
<!-- project-os:grounding-status=needs-input -->
```

- `ready` requires confirmed project purpose, whole-project stage, immediate project objective, and sufficient project-level source authority.
- `needs-input` preserves missing core facts explicitly and triggers `READY_WITH_GAPS`.
- Every non-governance source has a declared scope and authority boundary.
- The user can distinguish confirmed facts, ordinary evidence, agent recommendations, and unknowns.

## Contamination checks

- `AGENTS.md` contains cross-task collaboration rules and project-wide operational safeguards, not business workflow details.
- `AGENTS.md` does not contain task stages, checklist IDs, feature requirements, launch steps, subscription plans, or similar domain execution content.
- A task, checklist, issue, migration, launch, audit, or plan document is not the sole basis for project purpose, whole-project stage, immediate objective, or project decisions unless its project-level authority is explicit.
- `current_work.md` does not promote a work-item stage into the whole-project stage.
- `decision_log.md` does not promote task-level choices into project-level decisions.
- `artifact_index.md` states what each non-governance source owns and must not determine.

## Placement checks

- `AGENTS.md` declares the confirmed root and future-asset placement policy.
- `artifact_index.md` declares a directory map covering requirements, workstreams, research, generated outputs, background, and external sources as applicable.
- The root contains only governance entry points, confirmed project-level anchors, and tool-required files, or explicitly justifies exceptions.
- A new collaborator can determine where to create a confirmed requirement, draft requirement, active workstream plan, research note, generated report, and background document.
- Existing misplaced assets have a confirmed disposition: keep, relocate, archive, externalize, or needs confirmation.
- No empty directory exists solely to represent a hypothetical future domain.
- Archive material is non-authoritative and not loaded during ordinary cold start.
- Relocated assets have updated links, index entries, and substantive history.

## Semantic checks

### Collaboration rules

- Defines read-before-write behavior.
- Defines cold-start order.
- Defines update routing by meaning.
- Defines how to handle incomplete context, conflicting sources, and sensitive material.
- Does not contain volatile project status.
- Defines the project-level versus task-level promotion boundary.
- Defines root hygiene and future-asset placement without embedding domain content.

### Stable context

- Explains project purpose, current scope, stable constraints, and major modules or workstreams.
- Points to detailed facts.
- Does not accumulate task-level progress or historical narration.

### Current work

- States current stage, immediate objective, workstream status, blockers, decisions needed, and handoff.
- Avoids duplicating live issue, QA, owner, build, or test-case ledgers.
- Removes completed work that no longer affects the current stage.

### Durable decisions

- Contains only confirmed, long-lived choices.
- Records rationale, impact, reversal conditions, and detailed source.
- Keeps technical or product detail in the domain source.

### Artifact navigation

- Identifies current, historical, external, large, sensitive, and archived artifacts.
- Describes scope, owned facts, non-owned facts, authority, lifecycle, and physical placement without duplicating content or live progress.

### Effective history

- Records substantive changes in reverse chronological order.
- Excludes pure discussion, formatting-only edits, and failed intermediate attempts.

## Operational checks

- A collaborator can tell where to write a new fact before editing.
- A normal task does not require updating every governance file.
- External sources have clear authority and local-summary boundaries.
- Existing user files and worktree changes were preserved.
- No credentials or sensitive contents were read, copied, or logged.
- No code, Git, remote system, or deployment state changed outside the user's request.

## Cold-start test

Using the default three-role entry sequence, answer purpose, stage, objective, scope, blockers, handoff, and update routing. For detailed authority, decision, asset or history questions below, follow the documented conditional route; knowing where to look is sufficient before that task is triggered. Do not load every source or duplicate detailed answers into the entry files merely to pass this test.

Check these questions at the appropriate loading level:

1. What is the project and why does it exist?
2. What lifecycle stage is it in?
3. What is the immediate objective?
4. What is in scope and out of scope?
5. Where are product, technical, operational, legal, design, QA, and code truths?
6. What durable decisions are settled?
7. What is blocked or awaiting a decision?
8. What can a new collaborator pick up next?
9. Which assets are large, generated, sensitive, historical, or external?
10. Where should each likely future change be recorded?
11. Where should each likely new asset be physically created?

At `READY`, failure to answer questions 1–4 or 10 is a governance failure.

At `READY_WITH_GAPS`, the collaborator must be able to identify exactly which answers are unknown, why they were not inferred, which source or user confirmation would resolve them, and which safe work can continue.

Missing domain answers are acceptable only when the project genuinely lacks that domain or explicitly records the source as not yet registered.

### Focused repair and behavioral regression

For a status-only repair, verify the affected source and its directly relevant current references, the changed outcome, and the diff. Full inventory and unrelated domain acceptance are not required. Never treat the scenarios below as a mandatory interview with each project's user.

When changing this skill, test in disposable synthetic projects with no live external writes. Supply raw inputs and inspect decisions and artifacts, not exact headings or phrase matches. Use meaningful fixture checks for deterministic scripts, and separately label manual walkthroughs versus independently executed agent trials.

| Scenario input | Observable success | Failure to catch |
|---|---|---|
| New project with no assets yet | Real governance content; no speculative directories or fabricated decisions | Empty scaffold and predetermined multi-level tree |
| Existing README and ADR index own roles | Reuse registered owners; unrelated code/work remains unchanged | Duplicate context or decision files |
| User confirms feature released; old source says unimplemented | Current contradictory statuses reconciled within scope | Append completion yet retain pending status; invent test evidence |
| User confirms a next-version plan | Plan and released baseline remain distinguishable | Future behavior written as current runtime |
| User pauses an experiment | Removed from active blockers; restart boundary retained if useful | Claim access fixed or experiment permanently cancelled |
| Partial answer covers two documents, user skips a minor detail | One confirmation updates both; skipped detail does not reappear as a question | Repeated interview or unrelated work blocked |
| Known external source with current filters differing from an old note | Register direct source and scoped observation; do not overwrite desired contract | Re-ask for the source or equate a daily snapshot with full-cohort data |

For ablation, run the same representative task with only default entry sources, then add the relevant domain source when needed. Keep unrelated history and other domains withheld. The reduced context must preserve answers about purpose, current goal, boundaries, source routing, and the correct update target; a history question should deliberately load history rather than guess. Compare unnecessary reads/questions and touched files as costs, without imposing universal character or file-count thresholds. A dry-run walkthrough is not evidence that another agent executed these behaviors successfully.

## Result states

- **READY**: Structure is valid, core project facts are grounded, contamination and placement checks pass, and cold start is reliable.
- **READY_WITH_GAPS**: Structure is valid and contamination checks pass, but core onboarding facts, source authority, or placement policy remain incomplete.
- **INVALID**: Structural, safety, placeholder, contradictory-authority, or material contamination errors remain.

These are final, reviewed readiness states. The script's similarly named structural status is only one input; report unresolved semantic review separately rather than upgrading a declared marker into factual verification.

## Severity

- **Error**: Missing required role, broken cold-start path, unresolved placeholder, secret exposure, destructive overwrite, contradictory source ownership, invalid grounding marker, or confirmed task-to-project contamination.
- **Warning**: Missing grounding or placement marker in a legacy installation, overlong snapshot, thin artifact metadata, unclear external-source freshness, incomplete handoff, suspicious domain-source references in `AGENTS.md`, ordinary documents at the root needing placement review, or a role that may soon need splitting.
- **Suggestion**: Optional refinement that does not block reliable collaboration.
