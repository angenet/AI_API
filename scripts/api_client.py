"""AI API 客户端"""
import requests


# ====== API 配置 ======
PERPLEXITY_API_KEY = "pplx-16551wqPDCy1h7l1ZL5iMHDyWw2frj4iX8JmzUcYqdWsdA"
GROQ_API_KEY = "gsk_8rikqobrEqCfpKrT2fIbyGXohv741LUMP"


def call_llm(prompt, provider='openai'):
    endpoints = {
        "perplexity": "https://api.perplexity.com/v1/chat/completions",
        "groq": "https://api.groq.com/v1/chat/completions",
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
