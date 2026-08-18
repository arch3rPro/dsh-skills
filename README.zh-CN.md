<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="dsh-skills — 由 DeepSeek Harness 提炼的编码智能体技能，涵盖架构、测试、文档与流程四大类">
</p>

<div align="center">

# DeepSeek-Harness-Skills

</div>

<div align="center">

一套由 **DeepSeek Harness** 的工程约定提炼而成的编码智能体技能——即你的编码智能体在编码、评审、测试或撰写文档时自动应用的“可执行标准”。

</div>

<p align="center">
  <a href="./README.md">English</a> · <b>简体中文</b>
</p>

## 快速开始

用 skills.sh 安装器安装整套技能，然后选择你想要的技能与目标智能体：

```bash
npx skills@latest add arch3rPro/dsh-skills
```

或者直接读其中一个——每份 `SKILL.md` 都是一份自包含的可执行标准。按你正在做的事挑选对应的规范：[code-conventions](docs/architecture/code-conventions.md)、[testing-tiers](docs/testing/testing-tiers.md)、[prose-standard](docs/documentation/prose-standard.md)，或[技能全集](#技能全集)中的任意一个。

## 技能全集

共十个技能，覆盖四大类。全部为**模型触发（model-invoked）**——当触发器命中时，智能体会自动启用它们。

| 技能 | 类别 | 作用 |
| --- | --- | --- |
| [defensive-patterns](docs/architecture/defensive-patterns.md) | 架构 | 面向生命周期、并发、清理与不可信 I/O 的缺陷类规则 |
| [code-conventions](docs/architecture/code-conventions.md) | 架构 | 可逆副作用、显式优于隐式、配置优于硬编码、品牌化 ID |
| [extension-points-and-seams](docs/architecture/extension-points-and-seams.md) | 架构 | 仅当某能力存在多种实现或消费方时，才建立接缝（契约/实现/消费方） |
| [testing-tiers](docs/testing/testing-tiers.md) | 测试 | 选对测试层级、测试真实入口路径、验证外部世界而非组件自报 |
| [prose-standard](docs/documentation/prose-standard.md) | 文档 | 契约优先的散文：保留完整命题、删去推理记录 |
| [documentation-placement](docs/documentation/documentation-placement.md) | 文档 | 每个事实只有一个家；区分教程与参考；预算只作护栏 |
| [decision-records](docs/process/decision-records.md) | 流程 | 带分类、生命周期与必选"备选方案"的 ADR |
| [minimal-evidence-checks](docs/process/minimal-evidence-checks.md) | 流程 | 覆盖改动的最小检查集；修复或解释失败而非赌 CI |
| [code-review](docs/process/code-review.md) | 流程 | 双轴（规范 + 需求）；几个有实据的阻断项胜过一长串吹毛求疵 |
| [pr-history-hygiene](docs/process/pr-history-hygiene.md) | 流程 | 带租约保护的历史重写、审慎打标签、原生栈式合并 |

## 测试版（开发中）

另有五个源自 DeepSeek Harness 的规范仍在开发中。它们可通过 `npx skills` 安装，但尚未进入官方插件包。

| 技能 | 类别 | 作用 |
| --- | --- | --- |
| [postmortem](docs/process/postmortem.md) | 流程 | 失败复盘：执行摘要、根因、护栏 |
| [runtime-invariants](docs/testing/runtime-invariants.md) | 测试 | 只断言权威状态，而非服务/方法存在；启动即失败 |
| [responding-to-review-on-a-stack](docs/process/responding-to-review-on-a-stack.md) | 流程 | 在引入问题的 PR 上修复、向上游传播、重写后复审 |
| [event-contract-matrix](docs/documentation/event-contract-matrix.md) | 文档 | 记录每个事件的产生者与监听者，含绕过点 |
| [module-layering](docs/architecture/module-layering.md) | 架构 | 推导并强制模块依赖分层 |

## 来源

每个技能都由 DeepSeek Harness 中的真实约定提炼而成，并适配到任意代码库——而非只能在它来源的框架内使用。

## 如何打包

每个技能是独立的 `<类别>/<名称>` 目录，一次改动同时承载三个文件：

- `SKILL.md` — 可执行标准（Claude Code / 任意智能体框架）
- `agents/openai.yaml` — Codex 元数据与调用策略
- `docs/<类别>/<名称>.md` — 面向人的文档页

```text
skills/
  architecture/  代码如何成型、故障如何处理
  testing/       行为如何被验证
  documentation/ 散文与文档如何撰写
  process/       代码周边的工作流——决策、评审、检查、git
```

## 调用设计

技能分为**模型触发**（触发器命中时智能体自动启用）或**用户触发**（只有人输入技能名才会触发——零上下文开销，但人本身成了索引）。本仓库十个技能全部为模型触发。

## 安装

以下两种方式互斥，任选其一即可（不是叠加）。

### `npx skills` —— 任意智能体（Claude Code、Codex 等）

逐个安装技能（整套见[快速开始](#快速开始)）：

```bash
npx skills@latest add arch3rPro/dsh-skills --skill=code-review
```

> `npx skills` 从 GitHub 拉取——请先发布仓库，再运行上面的命令。

### Claude Code —— 插件

把本仓库添加为 Claude Code 插件市场，再安装插件：

```bash
claude plugins marketplace add arch3rPro/dsh-skills
claude plugins install dsh-skills@dsh-skills
```

插件清单位于 `.claude-plugin/`（`marketplace.json` 与 `plugin.json`）。

## 致谢

- **[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)** — 由 DeepSeek AI 开发的开源智能体框架。
- **[mattpocock/skills](https://github.com/mattpocock/skills)** — Matt Pocock 的面向真实工程实践的智能体技能。
