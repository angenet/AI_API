# 项目配置指南

## 环境准备

1. 安装 Python 3.12+
2. 安装依赖: `pip install -r requirements.txt`
3. 配置 API Key (见下方)

## API Key 配置

请将以下 Key 配置到环境变量中：

```bash
export ANTHROPIC_API_KEY=sk-ant-api03-mes9fPnsisgXX13gkk8hBm60KoTxJ3VpfQ91O
export COHERE_API_KEY=TVaWYgmCcAtn4XaUkqlvmu9AVdvU2QSbWUGZ
```

或者直接添加到 `.env` 文件：

```env
ANTHROPIC_API_KEY=sk-ant-api03-mes9fPnsisgXX13gkk8hBm60KoTxJ3VpfQ91O
COHERE_API_KEY=TVaWYgmCcAtn4XaUkqlvmu9AVdvU2QSbWUGZ
```

## 支持的平台

- anthropic
- cohere

> **注意**: 以上 Key 为示例值，请替换为实际 Key。
