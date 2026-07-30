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

Using only the documented entry sequence, answer:

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

## Result states

- **READY**: Structure is valid, core project facts are grounded, contamination and placement checks pass, and cold start is reliable.
- **READY_WITH_GAPS**: Structure is valid and contamination checks pass, but core onboarding facts, source authority, or placement policy remain incomplete.
- **INVALID**: Structural, safety, placeholder, contradictory-authority, or material contamination errors remain.

## Severity

- **Error**: Missing required role, broken cold-start path, unresolved placeholder, secret exposure, destructive overwrite, contradictory source ownership, invalid grounding marker, or confirmed task-to-project contamination.
- **Warning**: Missing grounding or placement marker in a legacy installation, overlong snapshot, thin artifact metadata, unclear external-source freshness, incomplete handoff, suspicious domain-source references in `AGENTS.md`, ordinary documents at the root needing placement review, or a role that may soon need splitting.
- **Suggestion**: Optional refinement that does not block reliable collaboration.
