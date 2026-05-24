"""AI API 客户端"""
import requests


# ====== API 配置 ======
KIMI_API_KEY = "sk-kimi-gpa7csHTbPxFDyTsfuuhICflXEX7x"
FIREWORKS_API_KEY = "fw_iOx2mtbjsYhOHuaYW9lVZLE5FBSsFJUrw"
BAICHUAN_API_KEY = "sk-sp-4TOQk3MlxeFKnzKM7dscfdGkvy4OTrfQ"
VOYAGE_API_KEY = "sk-voyage-fJhMnHBvmx7EIwedw8jJhu8M1Rw7bi"


def call_llm(prompt, provider='openai'):
    endpoints = {
        "kimi": "https://api.kimi.com/v1/chat/completions",
        "fireworks": "https://api.fireworks.com/v1/chat/completions",
        "baichuan": "https://api.baichuan.com/v1/chat/completions",
        "voyage": "https://api.voyage.com/v1/chat/completions",
    }
    headers = {
        'Authorization': f'Bearer ' + globals().get(f'{provider.upper()}_API_KEY', ''),
        'Content-Type': 'application/json',
    }
    # TODO: implement request
    pass


if __name__ == '__main__':
    # 测试调用
    print(f"Using key: {KIMI_API_KEY}")
    call_llm('Hello, world!', 'kimi')
