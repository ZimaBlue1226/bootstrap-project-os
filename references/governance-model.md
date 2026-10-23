# Project collaboration model

## What the system must accomplish

Agents lose conversational context, work in different environments, and encounter sources that change independently. A durable project needs a small amount of maintained state that lets the next collaborator make the correct decision without replaying history.

Judge a document by the decision it enables. Keep it when it has a continuing owner and purpose. A new document adds another place to search, update, and reconcile, so reuse an existing owner before creating one.

The useful optimization is reliable continuation with low reading and maintenance cost. Shortness alone is not success: deleting the reason for a constraint can make a concise document misleading.

## Project structure

| Layer | Responsibility | Typical owner |
|---|---|---|
| Collaboration | How to obtain context, act, coordinate, and update | Agent rules |
| Project context | Why the project exists, its scope and stable constraints | Context or an existing project overview |
| Handoff | What matters next and what prevents progress | Current work or an existing status source |
| Navigation | Where each relevant truth lives and when to read it | Source index |
| Domain facts | Requirements, design, architecture, policy, methods | The registered domain document or system |
| Implementation and operation | Code, execution status, configuration, observed behavior | Repository, tracker, or runtime system |
| History | What changed and the historical versions | Git or the owning system's version history |

These are responsibilities, not a required file tree. Four entry roles usually route to everything else. An existing README or tracker can serve a role; a small project can combine roles in clearly owned sections. Keep the cold-start route explicit.

## Authority is scoped

For a material claim, establish its subject and scope, its confirmation or observation basis, and whether it describes a current rule, a proposal, implementation, or observed operation. Use these dimensions to reason; do not impose a metadata table on every paragraph.

There is no universal ranking in which runtime, code, or a newer document overrides all other sources. A runtime observation can demonstrate a requirement violation without changing the requirement. A user can confirm deployment without supplying independent test evidence. Preserve both the confirmed state and the limits of the evidence.

Only confirmed project-level facts belong in stable context. A task's phase, checklist, or detailed requirement stays with that task or domain. A document's size, filename, date, or polish does not confer wider authority.

External canonical sources remain external. Register a direct reference, responsibility, relevant access boundary, and any observation date needed to interpret a snapshot. Read their current content before editing. An unavailable source remains unavailable; an old local export does not acquire its authority.

## Maintenance by responsibility

| Change | Destination |
|---|---|
| Stable project identity or principle | Context, with detailed rules in their domain source |
| Requirement, architecture, design, or policy | Its existing responsible source |
| Confirmed choice and its still-relevant rationale | Beside the rule it explains, or an existing purposeful ADR |
| Goal, blocker, or handoff | Current work, only to the extent needed for the next action |
| Owner, source, or path changes | Source index and affected references |
| Cross-task collaboration rule | Agent rules |
| Repeatable scenario-specific method | Existing runbook or method source |
| Automation or test behavior | Tool or code source |
| Detailed progress, assignee, or test case | Execution system |
| Edit history | Git or the owning system's version history |

For an authorized change, read the current owner, update its conclusion in place, reconcile directly relevant current references, and inspect the result. Keep context, dependencies, exceptions, and rationale that still affect action. Remove superseded explanations, repetitions, and temporary discussion. Historical claims may remain where useful, with their original scope and date.

Current work is a handoff, not the union of every old pending item. Completed items leave it when they no longer affect the next action. Paused work retains a restart condition only when useful. Partial completion closes only the confirmed scope. A skipped question stays unknown without becoming an invented blocker.

Separate delivered documentation, accepted design, merged code, tested behavior, and deployed operation. A future plan can coexist with today's baseline if the version boundary is clear.

## Decisions and history

A future collaborator usually needs the current rule and why it applies. Keep those together. Git records edits but does not automatically contain the reasoning behind a choice; migrate useful rationale into the owner before retiring a decision log.

Default to version history for change retrieval. Add a separate record only for a real consumer or obligation, such as user-facing release notes, a maintained ADR process, a regulatory record, or an external action without an adequate audit trail. Keep external operation evidence in the responsible source or existing handoff when it affects continuation. Do not record every action in a universal project ledger.

## Boundaries and growth

Start with existing sources. Split a document when distinct responsibilities repeatedly change independently or a real retrieval problem prevents use. Create directories only for actual content and group files when dependencies, ownership, or access require it.

Use agent rules for cross-task constraints, runbooks for conditional procedures, and tools for repeatable actions. A one-off execution does not justify additions to all three.

For execution spaces and agent coordination, read [collaboration.md](collaboration.md). For placement and retirement, read [asset-placement.md](asset-placement.md). For older installations, read [migration.md](migration.md).
