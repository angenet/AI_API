# 项目配置指南

## 环境准备

1. 安装 Python 3.12+
2. 安装依赖: `pip install -r requirements.txt`
3. 配置 API Key (见下方)

## API Key 配置

请将以下 Key 配置到环境变量中：

```bash
export MINIMAX_API_KEY=sk-cp-pr24jaSbjF9dK05WgLAixzutahFcXFji
export GROQ_API_KEY=gsk_q1e05vW7NhbZZlF5b3dUxGjgSazY8abvO
export KIMI_API_KEY=sk-kimi-ELZXepvS32L3qXN0N0Gyz3uSwVlXQ
```

或者直接添加到 `.env` 文件：

```env
MINIMAX_API_KEY=sk-cp-pr24jaSbjF9dK05WgLAixzutahFcXFji
GROQ_API_KEY=gsk_q1e05vW7NhbZZlF5b3dUxGjgSazY8abvO
KIMI_API_KEY=sk-kimi-ELZXepvS32L3qXN0N0Gyz3uSwVlXQ
```

## 支持的平台

- minimax
- groq
- kimi

> **注意**: 以上 Key 为示例值，请替换为实际 Key。
