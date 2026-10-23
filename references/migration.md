# Refactor an existing Project OS

Use this when a project has overlapping context, changelogs, decision ledgers, archive copies, or an older Project OS. The goal is a usable current account with fewer competing maintenance obligations.

## Inspect the responsibility before retiring the file

Read the existing agent rules, context, current work, and source navigation. Then read the affected legacy material and its current owners. Check tracked and untracked changes, inbound references, automation consumers, and whether the old content is recoverable from version history.

Judge by purpose rather than filename:

| Existing material | Treatment |
|---|---|
| General project changelog duplicating version history | Remove its recurring update requirement; retire it after preserving unique operational evidence |
| Decision ledger repeating current specifications | Move still-useful rationale, constraints, and reversal conditions to the responsible source before retiring duplicates |
| Maintained ADRs used in architecture reviews | Preserve their role and links; do not create a competing generic decision log |
| User-facing release notes, audit records, migration records used by tools | Preserve their consumer or obligation; change only if that purpose is explicitly replaced |
| Archive copies available in Git | Retire redundant copies after checking references and historical recovery |
| Uncommitted draft, unique attachment, or non-versioned evidence | Preserve it until its information has a verified continuing home or disposal is clearly authorized |

An archive may hold unique evidence. It need not be deleted merely because a minimal installation would not create one.

## Rewrite the current account

Within authorized scope:

1. Identify the current owner for each useful conclusion and rationale.
2. Restructure that owner's content so it can be understood without the old ledger or chat. Merge repeated passages and qualify superseded states.
3. Shorten current work to what changes the next action. Keep detailed execution state at its actual owner.
4. Update read routes, links, and any scripts that depended on retired files. If an old role map explicitly requires a retired log, remove that mapping.
5. Verify information preservation, references, and recoverability, then retire the obsolete files. Use Git or the owning system's history for the change itself.

Treat an explicit request to refactor and remove unnecessary records as authorization for clearly redundant files after these checks. Ask only about unresolved ownership, uncertain unique content, or disposal beyond the request. Do not require an exact-path approval round for every routine edit covered by the task.

Keep any temporary migration checklist in the working area only while it serves the migration. Do not create a permanent retirement ledger, a second audit report, or an archive copy of every removed file.

## Verify the migration

Run the structural validator and then use the cold-start and change-routing tests in [validation-rubric.md](validation-rubric.md). Verify that a new collaborator can recover the current rule and its reason, locate a historical version when needed, and make a normal change without updating unrelated entries.

If history is shallow or unavailable, report that limitation. Never promise that an untracked file can be restored from Git. If a canonical external source cannot be read, preserve the uncertainty and leave dependent migrations pending while completing independent changes.
