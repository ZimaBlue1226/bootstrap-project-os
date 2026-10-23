# bootstrap-project-os

[中文](README.zh.md) | [English](README.md)

用于建立或重构项目协作机制的 Codex 技能，让不同 agent、设备和会话能接续工作，同时减少重复维护。

第一性目标是让没有历史聊天的新协作者找到当前目标、负责来源和下一步，并知道自己可以改什么。文档数量、目录复杂度和记录频率都不代表协作质量。

## 核心分工

| 责任 | 默认来源 | 维护内容 |
|---|---|---|
| 协作规则 | `AGENTS.md` | 阅读顺序、操作边界、协作方式、更新路由 |
| 稳定背景 | `project_context.md` | 项目定位、范围、稳定原则和系统边界 |
| 当前接续 | `current_work.md` | 当前目标、实际阻塞和下一步 |
| 来源导航 | `artifact_index.md` | 谁负责什么、何时读取、访问限制和资产位置 |

这是四项责任，不要求额外创建四个同名文件。已有 README、状态文档、索引或外部系统可以继续负责。通常先读协作规则、背景和当前工作，再按任务通过索引查详细来源。

决策结论和仍有用的理由维护在负责正文中。修改历史交给 Git 或文档系统。不默认建立总 changelog、独立决策流水、归档副本或迁移台账。已有 ADR、面向用户的发布说明、审计记录如有独立用途，继续保留。

需求、设计、代码、执行状态和运行观察分别回答各自的问题。来源权威按范围确定，不用一条全局优先级把它们混为一谈。

## 使用

```text
使用 $bootstrap-project-os，根据当前项目已有来源建立可持续的协作机制。
```

```text
使用 $bootstrap-project-os 审计当前项目，只报告影响实际协作的问题，不修改文件。
```

```text
使用 $bootstrap-project-os 重构这个旧项目的协作机制。保留有用事实和理由，移除重复维护，并验证冷启动和后续更新是否可用。
```

Bootstrap 建立缺失的入口。Onboard 补齐影响工作的事实。Audit 只读。Repair 在授权范围内重构现有机制。

迁移旧项目时先读现行来源，按责任整理成完整的当前正文，再核对引用、工具依赖、独有信息和历史恢复能力，最后退役冗余材料。不会因为文件叫 changelog 就机械删除，也不会把参考项目的业务规则、本机路径或发布约定搬过来。

## 安装与升级

本仓库需要对应 GitHub 访问权限。仓库根目录就是技能包，现有个人技能目录可使用：

```bash
git clone https://github.com/ZimaBlue1226/bootstrap-project-os.git ~/.codex/skills/bootstrap-project-os
```

已经安装时，先核对远端、分支、本地提交和未提交内容。干净且没有本地提交的检出可以 fetch 后快进到指定远端分支；存在本地改进时先保留、核对并整合。

更新技能不等于另一个项目已完成迁移。取得新版技能后，在目标项目执行 Repair。[迁移指南](references/migration.md)负责旧日志和文档的保留、合并与退役方法。

## 检查与验证

脚本使用 Python 3.12 及以上版本和标准库。

```bash
python scripts/inspect_project.py --root <项目根目录>
python scripts/validate_project_os.py --root <项目根目录> --json
python -B -m unittest discover -s scripts/tests -v
```

检查器只读目录元数据，跳过敏感、大资产区域、链接和独立仓库；项目自身有更严格限制时优先遵守。

校验器只读职责入口，不修改项目。JSON 的 `status` 为 `valid` 或 `invalid`，`structure_status` 为 `pass` 或 `fail`，`semantic_status` 始终为 `not_checked`。退出码 0 表示结构有效，1 表示结构错误，2 表示命令参数或根目录不可用。外部来源只登记，不会自动抓取。

这一结构结果替代旧版脚本的 `ready|ready_with_gaps|invalid`。完成真实来源核验和冷启动测试后，交付结论仍可使用 `READY`、`READY_WITH_GAPS`、`INVALID`，但不能由文件齐全推定事实正确。缺少旧版标记、总日志或决策流水不再构成缺陷。

已有等价来源可通过 AGENTS 中的可选映射声明。旧版已明确映射且仍有用途的决策或历史来源继续受支持，格式见[验证说明](references/validation-rubric.md)。

受限环境运行测试时，将进程的标准 `TMP`、`TEMP` 指向可写临时目录。测试会在其中创建并清理隔离的合成项目。

## 维护技能

`SKILL.md` 是 agent 入口；references 保存按场景读取的方法；四份模板辅助建立缺失来源；scripts 负责确定性的检查。这两份 README 面向使用者。

实质修改需通过脚本回归，并在新项目与已有项目上执行隔离场景验证。检查实际决策和产物，尤其是理由是否丢失、无关文件是否被改动。文字匹配和结构通过不能替代行为验证。

分别核对源仓库、已安装副本和远端版本。按授权发布，确认远端实际提交，并说明哪些副本已经更新。
