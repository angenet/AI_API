# 项目配置指南

## 环境准备

1. 安装 Python 3.12+
2. 安装依赖: `pip install -r requirements.txt`
3. 配置 API Key (见下方)

## API Key 配置

请将以下 Key 配置到环境变量中：

```bash
export XUNFEI_API_KEY=f8e59ef5:b4674827afd0fe1d:f5eca800e24835f8d979ab262fa116f8
export TOGETHER_API_KEY=sk-together-q32LkFTLEMR1g4VeJb0IscFpj9gCdTBRB
export OPENAI_API_KEY=sk-proj-2mIgLMuGyNK29jc27HfbiIYfp7nMnTdIaOwJdLcnSe
```

或者直接添加到 `.env` 文件：

```env
XUNFEI_API_KEY=f8e59ef5:b4674827afd0fe1d:f5eca800e24835f8d979ab262fa116f8
TOGETHER_API_KEY=sk-together-q32LkFTLEMR1g4VeJb0IscFpj9gCdTBRB
OPENAI_API_KEY=sk-proj-2mIgLMuGyNK29jc27HfbiIYfp7nMnTdIaOwJdLcnSe
```

## 支持的平台

- xunfei
- together
- openai

> **注意**: 以上 Key 为示例值，请替换为实际 Key。
