# Reusable project-governance model

## Contents

1. Core principles
2. Promotion firewall
3. Logical and physical routing
4. Semantic roles
5. Lifecycle routing
6. Source authority
7. Scaling rules
8. Common failure modes

## Core principles

### Separate state, work, decisions, history, and navigation

These information types change at different rates and answer different questions. Keep them in separate semantic roles even when a very small project combines two roles into one file.

### Maintain one authoritative source per fact

A summary or index may point to a detailed source but must not become a competing copy. When two files disagree, explicitly select the authority or leave the conflict unresolved for a human decision.

### Optimize for cold starts and handoffs

A new collaborator should learn the project by following a short documented sequence rather than recursively searching the repository or relying on chat history.

### Route changes by meaning

Update a document because its owned fact changed, not because its filename was mentioned. Most tasks should affect only one or two governance files.

### Preserve uncertainty

Label proposals, inferred facts, unverified statements, and pending decisions. Do not rewrite them as settled truth.

## Promotion firewall

Classify a fact independently by scope, authority, and time horizon before routing it.

| Dimension | Values |
|---|---|
| Scope | Project, domain/module, workstream, task/checklist, reference/archive, unknown |
| Authority | User-confirmed, explicitly canonical, source-declared, external runtime, ordinary evidence, inferred/proposed, disputed |
| Time horizon | Stable, current project work, execution detail, durable decision, effective history |

Use these minimum gates:

```text
Stable project truth = project scope + confirmed authority + stable horizon
Current project work = project scope + confirmed authority + current-project horizon
Project decision     = project scope + explicit confirmation + durable choice
Cross-agent rule     = cross-task collaboration or project-wide operational safeguard
```

A document's filename, detail, recency, polish, or uniqueness does not establish project-level authority. Treat a Checklist, Task, Todo, Issue, plan, launch guide, migration note, and similar artifact as task-scoped until its broader ownership is explicitly confirmed.

If a gate fails, keep the fact in its existing source, index its boundary, or preserve it as an onboarding gap. Do not promote it.

## Logical and physical routing

Every material asset needs two independent routes:

```text
Logical route  = which facts the asset owns
Physical route = where the asset lives
```

Correct logical authority does not guarantee correct placement. A background document at the root can appear project-critical even when `artifact_index.md` labels it non-authoritative.

Use the project's existing coherent structure when possible. Otherwise apply the minimal baseline in `asset-placement.md`. Reserve the root for governance entry points, confirmed project-level anchors, and tool-required files.

After the user confirms the placement policy:

- Route new assets automatically when their role is unambiguous.
- Ask only when multiple destinations are plausible or authority would change.
- Require authorization before moving, renaming, deleting, or archiving existing assets.
- Update links, the artifact index, and effective history after relocation.

## Semantic roles

| Role | Answers | Default path | Must not become |
|---|---|---|---|
| Collaboration rules | How should agents and collaborators operate safely across tasks? | `AGENTS.md` | Business workflow, task status, project history, or domain specification |
| Stable context | What is the project now? | `project_context.md` | Changelog or task board |
| Current work | What matters now, what is next, and what is blocked? | `current_work.md` | Detailed issue or QA ledger |
| Durable decisions | What important choices are settled, why, and when may they be revisited? | `decision_log.md` | Full architecture or requirements spec |
| Artifact navigation | Where are authoritative, current, historical, external, large, and sensitive artifacts? | `artifact_index.md` | A duplicate of artifact contents |
| Effective history | What substantive changes have taken effect? | `changelog.md` | Discussion transcript or future plan |
| Detailed facts | What are the product, technical, legal, design, data, QA, or operational rules? | Project-specific | A second governance layer |
| Non-authoritative archive | What old, background, reference, or process material remains useful? | `archive/` | A source of current truth |

Default filenames are conventions, not mandatory authorities. Existing ADRs, roadmaps, READMEs, wikis, issue trackers, design systems, and specifications may fulfill a role.

For every non-governance source, record both what it owns and what it must not determine. This negative boundary prevents a valid task or domain source from silently becoming a project-wide authority.

## Lifecycle routing

| Change type | Primary destination |
|---|---|
| Stable identity, scope, capability, constraint, or current operating model | Stable context or detailed canonical source |
| Project phase, current objective, milestone, blocker, or handoff | Current work |
| Confirmed long-lived choice with alternatives or reversal conditions | Durable decision log, pointing to detail |
| Detailed requirement, architecture, protocol, design, policy, or acceptance rule | Domain-specific canonical source |
| Effective substantive change | Changelog |
| Artifact created, replaced, deprecated, relocated, or reclassified | Artifact index |
| Reusable cross-task safety or collaboration lesson | Collaboration rules |
| Research, superseded design, background, reference, or third-party process material | Non-authoritative archive |
| Routine issue, bug, test case, owner, live status, or build-specific note | The project's execution tracker |
| Pure discussion, failed experiment, or rejected draft with no continuing value | Usually nowhere; archive only when future reference is justified |

Recommended decision order:

```text
Identify the owned fact
→ update its canonical source
→ check whether current stage changed
→ check whether a durable decision formed
→ check whether artifact navigation changed
→ record the effective change if substantive
```

## Source authority

Use this precedence model unless the project defines another:

1. Runtime or production state explicitly designated as authoritative
2. Domain-specific canonical source
3. Durable decision record pointing to that source
4. Stable project snapshot
5. Current-work snapshot
6. Artifact index
7. Changelog
8. Archive, chat, and third-party summaries

Precedence does not make a lower layer useless. It defines how to resolve disagreement.

External systems can be authoritative. Record their URL or identifier, scope, access assumptions, and what local files may summarize them. Never silently replace an external source with a stale local copy.

## Scaling rules

- Start with the semantic roles needed for unambiguous handoff.
- Use the default full family for long-lived, multi-module, regulated, asset-heavy, or multi-collaborator projects.
- Reuse existing files when their ownership is already clear.
- Split a file when it repeatedly mixes facts with different owners or change rates.
- Add a wiki or retrieval layer only after source authority and lifecycle routing are stable.
- Keep execution details in the system where work actually happens; link rather than duplicate.

## Common failure modes

- One context file contains project identity, active tasks, decisions, file inventory, and history.
- A roadmap and current-work file both claim the same milestone status.
- A decision log contains full specifications that later drift.
- An artifact index contains live review progress or issue counts.
- A changelog records every edit, typo, and abandoned experiment.
- An archive is treated as current truth.
- Empty template files create the appearance of governance without usable context.
- Project-specific preferences are presented as universal governance rules.
- An agent infers owners, approvals, requirements, or business conclusions without confirmation.
- The only or largest document is treated as the project charter without confirming its scope.
- A work-item stage is copied into current work as the whole-project stage.
- Task-level choices are copied into the project decision log.
- `AGENTS.md` contains checklist IDs, launch steps, feature rules, or other business workflow details.
- Structural validation passes while project purpose, stage, objective, or source authority remains ungrounded.
- Background or superseded material remains at the root and gains false salience.
- A new requirement or workstream document is created at an arbitrary path because no placement policy exists.
- A generic directory tree replaces a coherent project-native structure.
- Empty directories are created for hypothetical future domains.
- External canonical sources are copied locally merely to fit the directory hierarchy.
