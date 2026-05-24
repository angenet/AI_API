# 项目配置指南

## 环境准备

1. 安装 Python 3.12+
2. 安装依赖: `pip install -r requirements.txt`
3. 配置 API Key (见下方)

## API Key 配置

请将以下 Key 配置到环境变量中：

```bash
export VOYAGE_API_KEY=sk-voyage-S15uZxl0mOnrUIWwvToDvOOrZwFS0P
export XIAOMI_TP_API_KEY=tp-XmQwSnr2q4aBjYsjMnv5mOpaaCypmjEK
```

或者直接添加到 `.env` 文件：

```env
VOYAGE_API_KEY=sk-voyage-S15uZxl0mOnrUIWwvToDvOOrZwFS0P
XIAOMI_TP_API_KEY=tp-XmQwSnr2q4aBjYsjMnv5mOpaaCypmjEK
```

## 支持的平台

- voyage
- xiaomi_tp

> **注意**: 以上 Key 为示例值，请替换为实际 Key。
