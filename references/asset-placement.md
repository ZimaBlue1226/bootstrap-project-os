# Asset placement and lifecycle

## Contents

1. Principles
2. Choose a placement profile
3. Recommended minimal baseline
4. Root-directory policy
5. Default routing examples
6. Existing-asset disposition
7. Future-asset behavior
8. Lifecycle transitions
9. External, large, generated, and sensitive assets
10. Persist the policy

## Principles

Treat logical authority and physical placement as separate decisions:

```text
Fact routing: what facts does this asset own?
Physical placement: where should this asset live?
```

A correct authority classification can still be physically misleading. Low-authority background material at the project root may appear more important than it is to people and shallow-discovery agents.

Use these rules:

- Prefer an existing coherent structure over a new generic hierarchy.
- Use the minimal standard baseline only when no reliable convention exists.
- Create directories lazily when the first real asset needs them.
- Keep one canonical location for each asset.
- Link to external canonical sources instead of copying them locally.
- Move existing assets only after user authorization.
- Once the user confirms the policy, place new assets automatically when routing is unambiguous.

## Choose a placement profile

Inspect root and shallow directory metadata. Identify existing conventions such as:

- `docs/`, `documentation/`, or a project wiki
- `product/`, `architecture/`, `design/`, `legal/`, `qa/`, or `operations/`
- `workstreams/`, `projects/`, `initiatives/`, `tasks/`, or an external tracker
- `research/`, `notes/`, `proposals/`, or `rfcs/`
- `assets/`, `media/`, `data/`, `artifacts/`, or external storage
- `archive/`, `history/`, or a document-versioning system

Recommend:

1. **Reuse** when the existing structure has clear ownership and lifecycle.
2. **Extend** when only one or two roles are missing.
3. **Adopt the minimal baseline** when the project has no coherent placement convention.
4. **External-first** when canonical documents or work status already live in GitHub, Feishu/Lark, Notion, Jira, Linear, a design system, or another authoritative tool.

Do not ask the user to design a directory tree. Present the detected convention or recommended baseline with one short confirmation.

## Recommended minimal baseline

Adapt names to the project's language and existing conventions:

```text
project-root/
├─ AGENTS.md
├─ project_context.md
├─ current_work.md
├─ decision_log.md
├─ artifact_index.md
├─ changelog.md
├─ docs/                        # maintained, confirmed domain sources
├─ work/                        # active research, plans, reviews, delivery material
├─ runbooks/                    # reusable conditional operating methods
├─ tools/                       # reusable scripts and tests
├─ assets/                      # local retained assets, when needed
├─ archive/                     # non-current material with independent history value
└─ .tmp/                        # disposable execution intermediates
```

The directories above are routing destinations, not an initialization checklist. Create each only with its first real asset; create `archive/README.md` only when the archive is used. Six governance roles are defaults for durable collaboration; reuse explicit existing role owners rather than producing duplicate files.

Start `docs/` and `work/` shallow. Names and document content often suffice; introduce subdirectories for a real ownership/access boundary, a demonstrated retrieval problem, or multi-file dependencies. Research, review, and execution are often phases of the same work, not three separate destinations. Preserve established `spec/`, `research/`, `workstreams/`, code, test, or external-first conventions when their responsibilities are already clear. Do not mechanically rename them to this baseline.

Code repositories keep tool-required structures such as `src/`, `tests/`, manifests, CI configuration, and framework directories. The Project OS supplements rather than replaces them.

## Root-directory policy

The root is a high-salience entry surface. Keep only:

- Project OS governance entry points
- A confirmed project-level overview such as `README.md`
- Toolchain, build, package, license, security, and contribution files required or conventionally expected at root
- Other explicitly justified project-level anchors

Review ordinary root-level requirements, task checklists, workstream plans, research notes, background documents, exports, and generated reports for relocation.

Root placement alone never grants authority.

## Default routing examples

| Asset | Default destination | Notes |
|---|---|---|
| Confirmed requirement, specification, architecture or durable QA rule | `docs/<topic>.md` or existing domain/ADR source | Split by actual ownership, not by synonymous document labels; live QA remains in its tracker |
| Design or legal source | Existing external authority or `docs/` | Respect access boundaries; create domain subdivisions when justified |
| Operations runbook | `runbooks/` or existing method source | Runtime state remains in the operational system |
| Reusable script or test | `tools/` or existing engineering tool location | Not a prose rule or temporary output |
| Active research, initiative plan, requirement draft or review | `work/<topic>.md` | Promote confirmed durable facts to their owner before retiring the work material |
| One-off task acceptance criteria | Execution tracker | Avoid creating a competing requirement document |
| Background, superseded material or retained external snapshot | `archive/` or established history location | Retain only independent history value; record provenance and replacement where applicable |
| Temporary script, upload copy or reproducible intermediate | `.tmp/` or existing temporary output area | Remove task-created unneeded files after verification within authorized cleanup scope |
| Generated report with independent delivery/evidence value | Its content owner or registered output location | Reproducibility alone does not make evidence disposable |

## Existing-asset disposition

For each material existing asset, propose:

| Disposition | Meaning |
|---|---|
| Keep | Current path already matches authority and lifecycle |
| Relocate | Asset remains current but belongs in another active location |
| Archive | Asset is background, superseded, or historical and non-authoritative |
| Externalize | Canonical truth belongs in an external system; keep only a link or minimal local pointer |
| Needs confirmation | Scope, authority, lifecycle, or target location is ambiguous |

Preview material changes:

```text
Current path:
Proposed path or external source:
Scope and authority:
Lifecycle:
Reason:
References that must be updated:
Effect on canonical ownership:
```

After approval, move with one filesystem mechanism, update links and `artifact_index.md`, remove stale path references, and record substantive reclassification in `changelog.md`.

## Future-asset behavior

After the placement policy is confirmed:

1. Identify the new asset's semantic role, scope, authority, and lifecycle.
2. Route it using the recorded directory map.
3. Create the narrowest required directory only when needed.
4. Register the asset when it becomes canonical, externally authoritative, large, generated, sensitive, relocated, or archived.
5. Ask only when multiple destinations are plausible, authority would change, or an existing asset must move.

Example:

```text
New confirmed requirement
→ docs/<requirement>.md or existing domain source
→ register as product-domain authority
→ link relevant work items
```

```text
New requirement draft
→ work/<requirement>.md or existing work source
→ promote to the canonical requirements location only after confirmation
```

## Lifecycle transitions

Common transitions:

```text
research or draft
→ confirmed domain truth
→ superseded
→ archive
```

```text
active workstream plan
→ completed handoff material
→ archive or remove if no continuing value
```

Do not archive merely because work is complete. Archive only when the material retains historical or background value. Delete or omit failed intermediate artifacts that have no continuing value, subject to user authorization.

Define exit conditions together with placement: maintained facts are updated or superseded; active work promotes durable outcomes then retires; methods/tools remain while reusable; temporary output is cleaned once no longer needed; archives retain independent evidence rather than all completed work. Within the project's cleanup authorization, remove only known task-created paths with no remaining use. For older material, verify ownership, references, and actual use first; never infer disposability from extension, directory name, or absence from an index. Do not follow links/junctions during cleanup.

Do not register every ephemeral intermediate or log cleanup as a substantive change. Migration disposition tables belong to the active migration source while useful, not permanently in the authority index. An execution being completed does not itself change the operating method or require a new runbook.

## External, large, generated, and sensitive assets

- Keep external canonical sources external. Record URL or identifier, ownership, access assumptions, and local-summary boundary.
- Do not move large assets into the standard tree merely for neatness. Register their actual location and loading boundary.
- Put reproducible generated outputs in the project's existing output convention and mark them generated.
- Do not move or open sensitive assets during placement. Record only their path and boundary.

## Persist the policy

Store:

- Concise future-placement rules and root policy in `AGENTS.md`.
- Detailed directory map, asset classification, lifecycle, and external boundaries in `artifact_index.md`.
- Stable canonical-source summary in `project_context.md` only when project-level facts changed.
- Project-level blockers in `current_work.md` only when placement gaps block current work.
- Effective relocations or reclassifications in `changelog.md`.

The placement policy must tell a future collaborator where to put a new requirement, workstream plan, research note, generated report, and background document without searching the whole project.
