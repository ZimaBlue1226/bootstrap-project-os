# Source-aware project onboarding

## Contents

1. Goal and stopping rule
2. Link-first intake
3. Source classification
4. Promotion firewall
5. Intake reflection
6. Placement confirmation
7. Installation states
8. After-install handoff

## Goal and stopping rule

Onboarding should establish enough confirmed project-level context for reliable cold starts without making the user learn governance terminology.

Collect or locate:

- Project identity and concise purpose
- Intended users or consumers when relevant
- Whole-project lifecycle stage
- Immediate project-level outcome
- Project-level canonical sources
- Execution and runtime sources
- Stable operational, approval, sensitive, and large-asset boundaries

Do not ask for facts already explicit in the request or a confirmed project-level source. Stop asking when remaining unknowns do not change source authority, safe operation, or the immediate cold-start route.

## Link-first intake

For new-project intake, after shallow inspection invite direct answers or existing sources. The fields below are a menu, not a mandatory questionnaire. For Repair, ask only for missing facts that change the current repair:

```text
I can build the project context from short answers or from sources you already have.
You may provide local paths or accessible links to repositories, README/product/architecture
documents, connected docs, public websites, task trackers, design or QA systems, and deployment
or operational tools.

Please tell me:
1. What is this project and who is it for?
2. What stage is the whole project in, and what outcome matters next?
3. Which sources describe the whole project, and which are only a task, checklist, module, or reference?
4. Where do code, work status, and runtime truth live, and what must not be read or changed?

"Unknown", "none yet", and "install the kernel first" are valid answers.
```

Adapt to the user's language. Mention discovered files by name only when their scope is ambiguous and material.

Examples:

```text
I found ios-launch-checklist.md. Does it describe the whole project or one work item?
```

```text
If the README and public website already explain the project, share or confirm them and I can
extract a proposed summary for your review.
```

When a source requires authentication, use an available connected app only within the user's request. Otherwise ask the user to connect it, export it, provide a local path, or summarize the relevant facts.

### Repair question triage

1. Establish current stage and immediate priorities before treating old review notes as active work. A stale pending label is a historical assertion, not proof of an unfinished task.
2. Check registered sources and prior answers first. Merge questions about the same business outcome even when several documents use different terms for it.
3. Ask in recognizable product or work language, describing the concrete missing fact rather than quoting an unexplained internal review label. Adapt question size to the user; one issue at a time when requested.
4. Ask only when the answer affects current scope, authority, safe action, or a material conclusion. Governance onboarding is not an exhaustive QA interview.
5. If the user skips an item, remove it from this round's question queue without declaring it resolved. Do not reintroduce it as a blocker unless it genuinely blocks the authorized next action; explain that dependency if it does.
6. Once an answer resolves several current references, reconcile those references within the authorized repair instead of requesting separate confirmations. Missing unrelated details do not block independent confirmed updates.

Stop when the current task can be completed safely and the remaining unknowns are merely future domain work. Do not automatically end every answer with another question.

## Source classification

Classify each relevant source on three independent axes.

### Scope

| Scope | Meaning |
|---|---|
| Project | Describes the whole project's identity, direction, or cross-cutting operating model |
| Domain or module | Owns a product, technical, design, legal, data, QA, or operational area |
| Workstream | Owns a multi-task initiative without defining the whole project |
| Task or checklist | Owns one execution item, launch, migration, audit, experiment, or todo set |
| Reference or archive | Supplies background, external guidance, or history |
| Unknown | Scope cannot yet be established safely |

### Authority

| Authority | Treatment |
|---|---|
| User-confirmed | May become truth in the appropriate scope |
| Explicitly designated canonical | May become truth within its declared ownership |
| Source-declared | Candidate authority; confirm if project-level impact is material |
| External runtime | Authoritative only for its live state and registered boundary |
| Ordinary evidence | Use for discovery; do not promote without confirmation |
| Inferred or proposed | Label and present for review |
| Disputed | Preserve the conflict and request resolution |

### Time horizon

| Horizon | Destination |
|---|---|
| Stable | Project context or domain source |
| Current project work | Current work |
| Execution detail | Task or execution tracker |
| Durable choice | Decision log after explicit project-level confirmation |
| Effective history | Changelog |

## Promotion firewall

The fact that a document is detailed, recent, polished, or the only document present does not establish project-level scope.

Promote only when all destination conditions are satisfied:

```text
Stable project truth
= project scope
+ user-confirmed or explicitly canonical authority
+ stable time horizon

Current project work
= project scope
+ user-confirmed or explicitly canonical authority
+ current project horizon

Project decision
= project scope
+ explicit confirmation
+ durable choice with impact or reversal conditions

Cross-agent rule
= cross-task collaboration or project-wide operational safeguard
```

If any required dimension is unknown, keep the fact in its existing source, index the boundary, or record it as an onboarding gap.

Business workflow details, task stages, checklist IDs, feature requirements, subscription plans, launch rules, and similar content do not belong in `AGENTS.md`.

## Intake reflection

Before writing a new authority mapping, reflect:

```text
Project:
Users or consumers:
Project stage and immediate outcome:
Proposed project-level sources:
Domain or module sources:
Workstream and task sources:
External runtime sources:
Sensitive, large-asset, and approval boundaries:
Existing structure and proposed placement policy:
Still unknown:
```

For every ambiguous source, state:

```text
Source:
Proposed scope:
Owns:
Must not determine:
Authority basis:
Confirmation needed:
```

Ask for one confirmation covering only material classifications. Do not force confirmation of obvious file creation or non-conflicting routing already authorized by the user.

## Placement confirmation

After source scope and authority are clear, show:

```text
Existing structure to reuse:
Recommended minimal additions:
Root-level assets to keep:
Assets proposed for relocation:
Assets proposed for archive:
External sources to keep external:
Future destination for requirements, workstreams, research, generated outputs, and background:
```

Ask for one confirmation of the policy and all material existing-asset moves. Do not ask the user to design directory names unless the project already has competing conventions.

Once confirmed, future assets follow the policy without repeated approval when the destination is unambiguous. Moving or archiving an existing user asset still requires authorization unless already covered by the confirmed placement preview.

## Installation states

Use three states:

### READY

- Governance structure is valid.
- Project purpose, whole-project stage, and immediate objective are confirmed.
- Project-level source authority is sufficient for cold start.
- Task and project boundaries are explicit.
- The physical placement policy is confirmed or an existing coherent structure is explicitly adopted.

### READY_WITH_GAPS

- Governance kernel and routes are usable.
- One or more core onboarding facts or source authorities remain unknown.
- The placement policy may also remain unconfirmed.
- Generated documents explicitly preserve those gaps.
- The user receives one concrete next-best fact or source to provide.

### INVALID

- Required roles or cold-start routes are broken.
- Placeholders remain.
- Authority is contradictory or task details have been promoted without basis.
- Sensitive content was exposed or destructive changes occurred.

Never report `READY_WITH_GAPS` as a complete bootstrap.

## After-install handoff

End with:

1. Exact cold-start order.
2. A sentence explaining that detailed sources are read only when a task touches their scope.
3. Validation state.
4. Remaining onboarding gaps.
5. Confirmed future-asset destinations.
6. One next-best action, such as registering the main repository, confirming the project charter, connecting the actual work tracker, or resolving one misplaced root asset.

When onboarding is incomplete, tell the user they can later say:

```text
Continue Project OS onboarding using the sources now available.
```
