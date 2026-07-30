# bootstrap-project-os

[English](./README.md) | [中文版](./README.zh.md)

A source-safe Codex skill for bootstrapping, onboarding, auditing, and repairing a durable local project collaboration OS.

It turns scattered project files and external sources into a small governance layer with explicit fact ownership, current-work tracking, decision history, asset placement, lifecycle routing, and a predictable cold start.

---

## Who reads what

This repository contains both human-facing documentation and agent-facing runtime instructions:

| Path | Audience | Purpose |
|---|---|---|
| `README.md` / `README.zh.md` | **Humans** | Overview, installation, usage, and maintenance |
| `SKILL.md` | **Codex** | Trigger metadata, operating boundaries, and the complete execution workflow |
| `references/` | **Codex, when needed** | Governance model, project adaptation, onboarding, asset placement, and validation rules |
| `assets/templates/` | **Codex output resources** | Adaptable templates for the generated Project OS |
| `scripts/inspect_project.py` | **Codex or maintainers** | Shallow, content-free project structure inspection |
| `scripts/validate_project_os.py` | **Codex or maintainers** | Deterministic Project OS validation |
| `agents/openai.yaml` | **Codex UI** | Display name, short description, and default invocation prompt |

> In one line: **README is for humans; `SKILL.md` is the runtime authority for the agent.**

---

## What it does

The skill supports four modes:

- **Bootstrap** — install a governance kernel where none exists.
- **Onboard** — connect project identity, confirmed facts, existing repositories, documents, websites, and trackers.
- **Audit** — identify authority, lifecycle, placement, and cold-start gaps without changing files.
- **Repair** — correct an existing Project OS without importing assumptions or unrelated business rules.

The generated system separates:

- stable project context;
- current project-level work;
- durable confirmed decisions;
- domain and work-item sources;
- artifact and directory placement;
- effective change history;
- external runtime truth;
- archives, large assets, and sensitive boundaries.

It also prevents a detailed task, checklist, launch guide, or historical document from silently becoming the definition of the whole project.

The skill does **not** modify product code, Git settings, remote systems, permissions, deployments, or task trackers unless the user separately requests those actions.

---

## Project OS model

The default governance kernel is:

```text
AGENTS.md
project_context.md
current_work.md
decision_log.md
artifact_index.md
changelog.md
archive/README.md
```

Its normal cold-start order is:

```text
AGENTS.md
→ project_context.md
→ current_work.md
→ decision_log.md
→ artifact_index.md
```

`changelog.md` is read only when effective history matters. Detailed domain sources are opened only when the current task touches their scope.

The physical project structure is adaptive. Existing coherent conventions are preserved. When no convention exists, the skill can propose a minimal baseline such as:

```text
docs/product/requirements/
docs/product/specifications/
docs/technical/
design/
legal/
qa/
operations/
workstreams/<initiative>/
research/
assets/
archive/background/
archive/superseded/
archive/external/
```

Directories are created lazily, only when a real asset needs them. Existing assets are moved or archived only after explicit authorization.

---

## Repository contents

The repository root is the skill package itself:

```text
bootstrap-project-os/
  README.md
  README.zh.md
  SKILL.md
  agents/
    openai.yaml
  scripts/
    inspect_project.py
    validate_project_os.py
  references/
    governance-model.md
    project-adaptation.md
    onboarding-protocol.md
    asset-placement.md
    validation-rubric.md
  assets/
    templates/
      AGENTS.md.template
      project_context.md.template
      current_work.md.template
      decision_log.md.template
      artifact_index.md.template
      changelog.md.template
      archive-README.md.template
```

There is no build step. The helper scripts use Python 3 and the standard library.

---

## Install

> This is a **private repository**. Your Git client must already be authenticated to GitHub and your account must have repository access.

### A. Manual install

Clone directly into your personal Codex skills directory:

```bash
git clone https://github.com/ZimaBlue1226/bootstrap-project-os.git ~/.codex/skills/bootstrap-project-os
```

Or install it for one project:

```bash
git clone https://github.com/ZimaBlue1226/bootstrap-project-os.git <project>/.codex/skills/bootstrap-project-os
```

The repository name, clone directory, and the `name` field in `SKILL.md` are all `bootstrap-project-os`; no wrapper directory or rename is required.

### B. Automated install

With a compatible cross-agent skill installer:

```bash
npx skills add https://github.com/ZimaBlue1226/bootstrap-project-os
```

Private-repository authentication is still required.

---

## Usage

Invoke the skill in natural language:

```text
Use $bootstrap-project-os to establish a durable local Project OS for this project.
```

You can also specify the mode:

```text
Use $bootstrap-project-os to audit this project without changing files.
```

```text
Use $bootstrap-project-os to repair the existing governance system and preserve current facts.
```

During onboarding, provide direct answers or point the skill at existing sources such as a GitHub repository, README, product brief, requirements document, architecture note, website, tracker, or connected document system. The skill will:

1. inspect the project shallowly;
2. summarize what it understood;
3. classify each source by scope, authority, and lifecycle;
4. propose any necessary asset placement;
5. request confirmation only for material authority or movement decisions;
6. install or repair the governance kernel;
7. validate the result as `READY`, `READY_WITH_GAPS`, or `INVALID`.

---

## Inspection and validation

Run the content-free structure inspector:

```bash
python scripts/inspect_project.py --root <project-root>
```

The inspector skips archives and common dependency, cache, build, large-asset, and sensitive areas. It reports paths and structural candidates without reading file contents.

Validate an installed Project OS:

```bash
python scripts/validate_project_os.py --root <project-root>
```

Use JSON output when integrating with another tool:

```bash
python scripts/validate_project_os.py --root <project-root> --json
```

Validation states:

- `READY` — structure, grounding, source boundaries, placement, and cold start are usable.
- `READY_WITH_GAPS` — the kernel is usable, but project facts or authority mappings still need input.
- `INVALID` — structural, placeholder, safety, or authority-boundary errors remain.

---

## Safety principles

- Project facts come only from the target project, accessible supplied sources, and user confirmation.
- Task details do not automatically become project-level truth.
- Archives are non-authoritative and excluded from ordinary discovery.
- Credential-like files are identified by path only and never opened.
- Existing files are not overwritten, moved, renamed, deleted, or archived without authorization.
- External sources are linked and bounded instead of copied locally without a reason.
- Existing coherent project structures take precedence over the recommended baseline.

---

## Maintaining the skill

Use the repository files according to their roles:

- change workflow and agent behavior in `SKILL.md`;
- change detailed governance logic in `references/`;
- change generated document shapes in `assets/templates/`;
- change deterministic inspection or validation behavior in `scripts/`;
- keep human-facing explanations in the two README files.

After modifying the skill, run:

```bash
python <skill-creator-dir>/scripts/quick_validate.py .
python scripts/validate_project_os.py --root <test-project>
```

Forward-test material changes against both an unstructured project and a project that already has a coherent directory system. Then commit and push so the installed package and private repository remain aligned.
