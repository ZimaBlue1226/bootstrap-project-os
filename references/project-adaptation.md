# Adapting the governance model to a project

## Contents

1. Evidence categories
2. Safe inspection
3. Source scope and authority
4. Role mapping
5. Information intake
6. Placement adaptation
7. Creation and migration rules
8. Environment adaptation

## Evidence categories

Keep four categories distinct throughout bootstrap:

| Category | Treatment |
|---|---|
| Discovered fact | Cite or point to the source; verify conflicts |
| User-confirmed fact | May become current truth in the appropriate source |
| Agent recommendation | Present as a proposal, never as project policy |
| Unknown or disputed item | Put in current-work decisions/blockers or ask the user |

## Safe inspection

Begin with root and shallow directory metadata. Do not start with recursive content search.

Skip dependency, cache, generated, VCS, binary-asset, dataset, model, build, and output directories unless an existing rule or artifact index directs otherwise.

Potential secrets include `.env*`, private keys, certificates, credentials, tokens, keystores, signing material, and files explicitly marked sensitive. Identify their locations without reading contents.

Read existing instructions before applying generic defaults. Repository-local rules outrank this skill for the target project unless they conflict with system or user instructions.

## Source scope and authority

Do not infer source scope from its filename or amount of detail. Classify each relevant source:

| Scope | Typical examples | May determine |
|---|---|---|
| Project | Confirmed charter, project handbook, project-level product brief | Whole-project identity and direction within declared ownership |
| Domain/module | Architecture spec, design system, legal policy, API documentation | Its own domain only |
| Workstream | Launch program, migration initiative, research track | That initiative only |
| Task/checklist | Todo list, issue, audit checklist, release checklist | Its own execution state only |
| Reference/archive | Public website, external guidance, old design, research | Evidence or history only |
| Unknown | Ambiguous document or inaccessible source | Nothing until clarified |

Record the authority basis separately:

- User-confirmed
- Explicitly designated canonical
- Source-declared but unconfirmed
- External runtime
- Ordinary evidence
- Inferred or proposed
- Disputed

Only user-confirmed or explicitly canonical project-scope sources may establish project-level truth. A public website may describe the product or expose live behavior, but it is not automatically the internal project charter.

In `artifact_index.md`, record each source's scope, owned facts, facts it must not determine, authority basis, and lifecycle.

## Role mapping

For each semantic role:

1. Find existing candidates.
2. Determine which candidate is actually maintained.
3. Check whether it mixes unrelated roles.
4. Reuse it if ownership is clear.
5. Create a default file only if the role is missing.
6. Record non-default mappings in the cold-start route.

Common equivalents:

| Role | Possible existing sources |
|---|---|
| Stable context | README, product brief, project charter, handbook |
| Current work | ROADMAP, STATUS, milestone document, project board |
| Durable decisions | ADR directory, RFC decisions, architecture decision log |
| Artifact navigation | docs index, catalog, manifest, data registry |
| Effective history | CHANGELOG, release notes, migration history |
| Detailed facts | requirements, architecture, API docs, design files, policies |
| Execution tracking | GitHub Issues, Jira, Linear, Base, spreadsheet, task system |

Do not merge roles merely because one existing filename resembles another role. Judge by actual ownership.

## Information intake

Use the link-first onboarding in `onboarding-protocol.md`. Invite the user to answer directly or provide existing sources, including local files, GitHub repositories, connected documents, public websites, task trackers, design systems, QA systems, or operational tools.

Read only necessary entry points, extract candidate facts, and reflect the proposed classification for confirmation. Do not make the user translate their information into governance terminology.

Ask only for material unknowns. Prefer one compact onboarding prompt, then one follow-up at a time when needed. Useful fields include:

- Project name and concise purpose
- Intended users or consumers when relevant
- Current lifecycle stage
- Immediate project-level objective
- Confirmed scope and stable constraints
- Existing canonical product, technical, design, legal, data, QA, and operational sources
- Work-tracking system
- Collaboration and approval model, only when the project needs it
- Large assets, generated outputs, and sensitive locations
- Default language, shell, encoding, or platform conventions when operationally relevant

Do not require every project to define product owners, feature-ID formats, compliance workflows, or release gates. Those are project-specific policies.

If the user says to install the kernel first or cannot answer, keep the missing facts explicit, set grounding status to `needs-input`, and report `READY_WITH_GAPS`.

## Placement adaptation

Read `asset-placement.md` before proposing directory changes.

Inspect existing top-level and shallow directory conventions. Prefer reuse or extension over replacement. When no coherent convention exists, propose the minimal baseline rather than asking the user to invent a hierarchy.

Classify each material existing asset as:

- Keep
- Relocate
- Archive
- Externalize
- Needs confirmation

Present one placement preview and request authorization for material moves. After the user confirms the policy, record it in `AGENTS.md` and the detailed directory map in `artifact_index.md`.

Do not create empty directories. Do not recursively inspect archive contents; read only the archive boundary unless the task explicitly requires history.

## Creation and migration rules

- Personalize every created document with known project facts.
- Keep unknowns explicit and centralized.
- Do not leave placeholder tokens.
- Put only project-scope confirmed facts in stable context and current work.
- Keep work-item status, stages, and choices in their work-item source.
- Keep business workflow details out of `AGENTS.md`.
- Keep concise root and future-asset placement rules in `AGENTS.md`; keep the detailed directory map in `artifact_index.md`.
- Place new assets according to the confirmed policy when classification is unambiguous.
- Update links, navigation, and effective history after relocation or archival.
- Do not create a folder solely to show a future possibility.
- Do not move existing material into `archive/` without authorization.
- Do not rewrite history to make the new governance system appear older than it is.
- Record the governance bootstrap itself as an effective change when a changelog is created.
- If detailed sources do not yet exist, describe their intended role without inventing their contents.
- If a file is overloaded, first define the destination roles, then migrate facts by ownership, then remove duplicates only after verification.

## Environment adaptation

Generate environment rules only from evidence or user confirmation:

- Operating system and shell
- Text encoding and line endings
- Repository layout and nested repositories
- Build, test, and deployment commands
- Branch and commit policy
- External applications and access assumptions
- Sensitive paths and large-asset exclusions

Never copy an environment workaround from a reference project merely because it worked there.
