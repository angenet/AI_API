# 项目配置指南

## 环境准备

1. 安装 Python 3.12+
2. 安装依赖: `pip install -r requirements.txt`
3. 配置 API Key (见下方)

## API Key 配置

请将以下 Key 配置到环境变量中：

```bash
export MINIMAX_API_KEY=sk-cp-jutSjBzhaJMvTj6NMNeo8cGObirZxMpv
export XIAOMI_TP_API_KEY=tp-lTjMGFOpvayIMj8CEqhU32ZDVVma2B1U
export HUGGINGFACE_API_KEY=hf_TY1afzaFn3Zi41PxIGvH7mqsgBRCF2FZj
```

或者直接添加到 `.env` 文件：

```env
MINIMAX_API_KEY=sk-cp-jutSjBzhaJMvTj6NMNeo8cGObirZxMpv
XIAOMI_TP_API_KEY=tp-lTjMGFOpvayIMj8CEqhU32ZDVVma2B1U
HUGGINGFACE_API_KEY=hf_TY1afzaFn3Zi41PxIGvH7mqsgBRCF2FZj
```

## 支持的平台

- minimax
- xiaomi_tp
- huggingface

> **注意**: 以上 Key 为示例值，请替换为实际 Key。
