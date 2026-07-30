# bootstrap-project-os

[中文版](./README.zh.md) | [English](./README.md)

一个强调事实源安全的 Codex skill，用于冷启动、引导接入、审计或修复持久的本地项目协作 OS。

它把散落的项目文件和外部来源整理成一层轻量治理系统，明确事实归属、当前工作、长期决策、资产落位、生命周期更新路由和冷启动顺序。

---

## 文件分工

本仓库同时包含给人看的文档和给 Agent 看的运行指令：

| 路径 | 读者 | 作用 |
|---|---|---|
| `README.md` / `README.zh.md` | **人** | 项目概览、安装、用法和维护说明 |
| `SKILL.md` | **Codex** | 触发元数据、操作边界和完整执行工作流 |
| `references/` | **Codex，按需读取** | 治理模型、项目适配、onboarding、资产落位和校验规则 |
| `assets/templates/` | **Codex 输出资源** | 生成 Project OS 时使用的可适配模板 |
| `scripts/inspect_project.py` | **Codex 或维护者** | 不读取内容的浅层项目结构检查 |
| `scripts/validate_project_os.py` | **Codex 或维护者** | 确定性的 Project OS 校验 |
| `agents/openai.yaml` | **Codex UI** | 展示名称、简短描述和默认调用提示 |

> 一句话：**README 给人看；`SKILL.md` 是 Agent 运行时的权威入口。**

---

## 它做什么

Skill 支持四种模式：

- **Bootstrap / 冷启动**——在缺少治理系统的项目中建立基础内核。
- **Onboard / 引导接入**——连接项目身份、已确认事实、现有仓库、文档、网站和任务系统。
- **Audit / 审计**——只报告事实源、生命周期、资产落位和冷启动缺口，不修改文件。
- **Repair / 修复**——在保留项目事实的前提下纠正已有 Project OS。

生成的系统会区分：

- 稳定的项目上下文；
- 当前项目级工作；
- 已确认的长期决策；
- 领域来源与工作项来源；
- 资产和目录落位；
- 已生效的变更历史；
- 外部运行时事实；
- 归档、大型资产和敏感边界。

它还会阻止详细的 Task、Checklist、上架指南或历史文档在未经确认时被误当成整个项目的定义。

除非用户另行明确请求，本 skill 不修改产品代码、Git 设置、远端系统、权限、部署或任务系统。

---

## Project OS 模型

默认治理内核为：

```text
AGENTS.md
project_context.md
current_work.md
decision_log.md
artifact_index.md
changelog.md
archive/README.md
```

常规冷启动顺序为：

```text
AGENTS.md
→ project_context.md
→ current_work.md
→ decision_log.md
→ artifact_index.md
```

只有需要了解已生效历史时才读取 `changelog.md`；只有当前任务涉及某个领域时才打开对应的详细事实源。

物理目录结构是自适应的：优先保留项目已有且合理的约定。没有清晰规范时，skill 可以建议以下最小基线：

```text
docs/product/requirements/
docs/product/specifications/
docs/technical/
design/
legal/
qa/
operations/
workstreams/<事项名称>/
research/
assets/
archive/background/
archive/superseded/
archive/external/
```

目录按需创建，只有出现真实资产时才建立。移动或归档既有资产前必须获得明确授权。

---

## 仓库结构

仓库根目录就是 skill 包本身：

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

无需构建步骤。辅助脚本使用 Python 3 和标准库。

---

## 安装

> 这是一个**私密仓库**。Git 客户端必须已经登录 GitHub，并且当前账号拥有仓库访问权限。

### A. 人工安装

直接 clone 到个人 Codex skills 目录：

```bash
git clone https://github.com/ZimaBlue1226/bootstrap-project-os.git ~/.codex/skills/bootstrap-project-os
```

也可以只为单个项目安装：

```bash
git clone https://github.com/ZimaBlue1226/bootstrap-project-os.git <项目目录>/.codex/skills/bootstrap-project-os
```

仓库名、clone 后的目录名和 `SKILL.md` 中的 `name` 都是 `bootstrap-project-os`，无需额外套一层目录或重命名。

### B. 自动安装

使用兼容的跨 Agent skill 安装器：

```bash
npx skills add https://github.com/ZimaBlue1226/bootstrap-project-os
```

私密仓库仍然要求本机已经配置好 GitHub 认证。

---

## 用法

用自然语言调用：

```text
使用 $bootstrap-project-os 为当前项目建立持久的本地 Project OS。
```

也可以明确指定模式：

```text
使用 $bootstrap-project-os 审计当前项目，只报告问题，不修改文件。
```

```text
使用 $bootstrap-project-os 修复现有治理系统，并保留已经确认的项目事实。
```

Onboarding 时，可以直接回答核心问题，也可以提供现成的 GitHub 仓库、README、产品文档、需求文档、架构说明、网站、任务系统或已连接的文档来源。Skill 会：

1. 浅层检查当前项目；
2. 复述它理解到的事实；
3. 按范围、权威性和生命周期分类来源；
4. 提议必要的资产落位；
5. 只在涉及重要事实升级或资产移动时请求确认；
6. 建立或修复治理内核；
7. 将结果校验为 `READY`、`READY_WITH_GAPS` 或 `INVALID`。

---

## 检查与校验

运行不读取文件内容的结构检查器：

```bash
python scripts/inspect_project.py --root <项目根目录>
```

检查器会跳过归档以及常见依赖、缓存、构建、大型资产和敏感区域，只报告路径和结构候选。

校验已安装的 Project OS：

```bash
python scripts/validate_project_os.py --root <项目根目录>
```

需要接入其他工具时可输出 JSON：

```bash
python scripts/validate_project_os.py --root <项目根目录> --json
```

校验状态：

- `READY`——结构、事实 grounding、来源边界、资产落位和冷启动均可用。
- `READY_WITH_GAPS`——治理内核可用，但仍缺少项目事实或权威关系确认。
- `INVALID`——仍存在结构、占位符、安全或事实边界错误。

---

## 安全原则

- 项目事实只来自目标项目、用户提供且可访问的来源，以及用户确认。
- 任务细节不会自动升级成项目级事实。
- 归档是非权威来源，不进入普通发现流程。
- 疑似凭据文件只按路径识别，不打开内容。
- 未经授权，不覆盖、移动、重命名、删除或归档既有文件。
- 外部事实源优先登记链接和边界，不为了适配目录而无理由复制到本地。
- 项目已有且合理的目录规范优先于推荐基线。

---

## 维护 skill

按文件职责修改：

- 在 `SKILL.md` 修改工作流和 Agent 行为；
- 在 `references/` 修改详细治理逻辑；
- 在 `assets/templates/` 修改生成文档的结构；
- 在 `scripts/` 修改确定性的检查或校验行为；
- 在两个 README 中维护给人看的说明。

修改后运行：

```bash
python <skill-creator目录>/scripts/quick_validate.py .
python scripts/validate_project_os.py --root <测试项目>
```

重大改动应同时用“根目录混放的项目”和“已有成熟目录结构的项目”进行前向测试。测试通过后再提交并推送，保持已安装 skill 与私密仓库一致。
