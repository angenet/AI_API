# 项目配置指南

## 环境准备

1. 安装 Python 3.12+
2. 安装依赖: `pip install -r requirements.txt`
3. 配置 API Key (见下方)

## API Key 配置

请将以下 Key 配置到环境变量中：

```bash
export TOGETHER_API_KEY=sk-together-UUAjDay5osyW4jXv5myyLiG083rmSPgAQ
export ZHIPU_API_KEY=bec1eb29f7a0a952.58d47182b36ed372
export FIREWORKS_API_KEY=fw_QVjyE5kvyQX3i8JnFWj9N6jCTUeTjxEwx
```

或者直接添加到 `.env` 文件：

```env
TOGETHER_API_KEY=sk-together-UUAjDay5osyW4jXv5myyLiG083rmSPgAQ
ZHIPU_API_KEY=bec1eb29f7a0a952.58d47182b36ed372
FIREWORKS_API_KEY=fw_QVjyE5kvyQX3i8JnFWj9N6jCTUeTjxEwx
```

## 支持的平台

- together
- zhipu
- fireworks

> **注意**: 以上 Key 为示例值，请替换为实际 Key。
