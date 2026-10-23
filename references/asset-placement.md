# Placement and lifecycle

Use the project's coherent existing layout. Physical location helps retrieval but does not confer authority; a draft in `docs/` remains a draft if that is its declared state.

## Minimal default

When no useful convention exists:

| Location | Responsibility | Exit or maintenance condition |
|---|---|---|
| Root entries | Collaboration rules, context, handoff, navigation, tool-required files | Update only the entry whose responsibility changed |
| `docs/` | Maintained local domain material, useful background, durable interactive examples | Rewrite current conclusions; retire material whose purpose ended |
| `runbooks/` | Confirmed repeatable procedures | Update when the reusable method changes |
| `tools/` | Reusable automation and tests | Maintain with behavior and dependency changes |
| `work/` | Drafts, candidate assets, or research requiring continuation | Extract adopted outcomes into their owner, then retain only useful unfinished work |
| `assets/` | Adopted local assets and design sources | Follow the project's delivery and versioning policy |
| `.tmp/` | Reproducible intermediates, temporary exports, one-off output | Remove after verification when no continuing use remains |

These are destinations, not directories to precreate. Start flat; group files when actual dependencies, ownership, or access need it. Preserve engineering structures and external-first conventions.

Large assets are not universally excluded from Git. Decide using the project's actual versioning, licensing, delivery, and storage conventions. A specific project's local drive layout is not a reusable default.

## Existing material

For each affected item, decide whether to keep it, consolidate it into an existing owner, relocate it, register an external owner, or retire it. Preview material moves and uncertain ownership changes. Continue within the user's existing authorization.

Before retiring or moving content, verify its current use, inbound references, tool dependencies, unique information, and historical recoverability. Never infer disposability from an extension or absence from the index. Untracked content is not recoverable merely because the project uses Git.

Update affected references after moves. Register only sources and assets that another collaborator needs to find; ephemeral outputs do not require index entries or a cleanup ledger.

## History and archives

Use version history for old committed copies. Do not create an archive directory or an archive-boundary document by default. Preserve an established archive when it contains useful unique evidence or serves a real retention need. Mark that boundary in the existing source index or archive entry and keep it out of ordinary cold start.

Completion alone does not determine disposal. A completed report can remain useful evidence, while a failed temporary export may have no continuing purpose. Preserve useful background in its existing or appropriate local source with a clear reference status.

## Access and cleanup

External canonical sources stay external; retain a direct reference and access boundary rather than a local mirror. Record sensitive locations without reading their content. Inspect large assets only at indexed paths required by the task.

Before recursive cleanup, resolve explicit absolute targets inside the intended workspace, reject links and junctions, and inspect the selected subtree for independent repositories and protected content. Use one filesystem mechanism, process only known paths, and avoid extension-wide deletion. Keep needed uncommitted work before cleanup.

Persist the simple placement policy once in agent rules or the existing index, with a pointer from the other. Add detailed asset locations only where needed. Do not repeat the directory policy in every entry.
