"""AI API 客户端"""
import requests


# ====== API 配置 ======
PERPLEXITY_API_KEY = "pplx-ynARCqRKXgdOY1Q5NBCeXAmfvY71WSECtGabhV9vGp5oj5"
XUNFEI_API_KEY = "839c786a:44287111fd208aed:d10a2a5b0fd43fa852dfcb7109e0ad08"
ANTHROPIC_API_KEY = "sk-ant-api03-CC84ZDA6Kh2kf8vGQrayb08ne5Fe6PO5ymkRS"
XIAOMI_TP_API_KEY = "tp-W5Gkz0Pey6VoShcoEJd3ZxUWLA100vxF"


def call_llm(prompt, provider='openai'):
    endpoints = {
        "perplexity": "https://api.perplexity.com/v1/chat/completions",
        "xunfei": "https://api.xunfei.com/v1/chat/completions",
        "anthropic": "https://api.anthropic.com/v1/chat/completions",
        "xiaomi_tp": "https://api.xiaomitp.com/v1/chat/completions",
    }
    headers = {
        'Authorization': f'Bearer ' + globals().get(f'{provider.upper()}_API_KEY', ''),
        'Content-Type': 'application/json',
    }
    # TODO: implement request
    pass


if __name__ == '__main__':
    # 测试调用
    print(f"Using key: {PERPLEXITY_API_KEY}")
    call_llm('Hello, world!', 'perplexity')
