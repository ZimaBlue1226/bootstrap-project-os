# Validate usefulness, not document ceremony

## Structural checks

Run `scripts/validate_project_os.py --root <project-root> --json` after structural changes. It reads declared role-owner files and writes nothing. It checks file presence, readability, placeholder replacement, source registration in AGENTS, and local path boundaries.

The script reports `status: valid|invalid`, `structure_status: pass|fail`, and always `semantic_status: not_checked`. This replaces the old automated `ready|ready_with_gaps|invalid` status. Consumers must use the new structural meaning; a successful script never certifies source accuracy or collaboration behavior.

Four roles have defaults: `collaboration_rules`, `stable_context`, `current_work`, and `artifact_navigation`. Existing owners can be registered in one optional JSON comment in AGENTS:

```text
<!-- project-os:role-map={"stable_context":"README.md","current_work":"STATUS.md"} -->
```

Only overrides are needed. Shared files are allowed when the sections and ownership are clear. `AGENTS.md` remains the local entry. Other roles may use project-relative files or HTTP/HTTPS URLs. External owners are registered but never fetched by this script; verify required access and scope separately.

The legacy keys `durable_decisions` and `effective_history` remain supported when explicitly mapped to a purposeful source. They are not default requirements. Remove mappings to retired logs during migration rather than creating empty replacement files.

Local role paths may not escape the project, traverse links or junctions, or enter sensitive, archived, generated, or independent repository locations. The validator does not scan domain documents or recursively validate every link. Read the relevant sources and inspect affected links as part of the actual task.

Old grounding markers are optional declarations, not proof. Missing markers produce no warning. A malformed or contradictory supplied marker is an error; `needs-input` is a review item. The old task-boundary and placement markers are not required. Neither file length, root placement, a runbook pointer, nor the absence of a changelog proves a defect.

## Cold-start check

Give a collaborator only the documented entry route and the authorized task. They should be able to explain:

- What the project is for, its boundaries, and the next useful outcome.
- Which facts are confirmed, proposed, observed, or unknown where that distinction matters.
- Which source to read before changing a requirement, implementation, or runtime state.
- What they can act on and what remains blocked by authority or access.
- Where a new conclusion belongs and whether any entry route also needs updating.

Let them follow the index when a domain question arises. Do not load all history or copy domain detail into context to make the test easier.

For cross-environment work, verify the branch and baseline, unsynchronized changes, independent repositories, unavailable assets or tools, and access assumptions. Do not infer environment readiness from the presence of a link.

## Change scenarios

Use the relevant scenarios, not an exhaustive interview or mandatory full suite for every repair.

| Scenario | Observable result |
|---|---|
| New project without domain material | Grounded context and useful routes; no invented decisions, speculative directories, or empty logs |
| Existing README, status board, ADRs, release notes | Reuse real owners; preserve distinct consumers and unrelated work |
| Legacy logs duplicate current facts | Preserve unique rationale and evidence in the owner, repair references, retire redundant obligations within authorization |
| Confirmed completion with old pending text | Reconcile current references; retain evidence limitations without calling the confirmed work unimplemented |
| Confirmed next-version plan | Keep today's operation and future intent distinguishable |
| Paused work or partial answer | Preserve the scope; do not invent a blocker or restart repeated questioning |
| Unavailable external authority | Report the access boundary; finish independent changes without promoting a stale export |
| Dirty checkout or independent repository | Preserve work and ownership; do not claim synchronization or publish without authorization |
| Domain rule changes with stable goal and sources | Change its owner; leave unrelated context, handoff, and navigation alone |
| Historical rationale is needed | Follow the registered source or version history; do not invent it from current text |

## Test the skill itself

Run deterministic tests for scripts and realistic behavior trials for material instruction changes. Keep those forms of evidence separate. Script tests should observe behavior, such as preservation of files, rejection before sensitive reads, correct role reuse, and failure on a missing owner. Do not test exact prose or preferred headings.

For a substantial refactor, use an independent subagent evaluation when delegation is available and authorized. Give it the skill, a realistic request, and minimal raw artifacts in an isolated temporary project. Withhold the intended answer, suspected defects, and proposed fixes. Keep live external writes out of the evaluation. Inspect its actual actions and outputs, then correct only demonstrated material failures.

Test both an unstructured project and an established project. For cold-start testing, begin with entries only and allow the documented conditional reads. Compare correct outcomes, unnecessary questions, unrelated reads, and touched files. There is no universal target for character counts or number of files.

## Reviewed outcome and stopping rule

Human-readable outcomes after semantic review:

- **READY**: The authorized scope has usable owners and routes, supported current conclusions, and a working cold start.
- **READY_WITH_GAPS**: Useful work can continue, but identified material facts or access still prevent a complete handoff.
- **INVALID**: A broken route, material contradiction, information loss, unsafe read or write, or unsupported authority change remains.

State the tested scope and limitations. Merely registering an external URL is not a successful read. A walkthrough is not an independently executed trial.

Fix issues that can change an action or conclusion. Treat aesthetic preferences as optional. Stop when the intended outcome and relevant checks pass; do not add work to eliminate every possible future concern.
