"""AI API 客户端"""
import requests


# ====== API 配置 ======
PERPLEXITY_API_KEY = "pplx-eWBk4hmLVBpfF9hY1ZusY4UwuLBnxIoHiZTPX0imPJlALp"
XUNFEI_API_KEY = "770bcd10:fbb0daf718592b80:8a0936cc849bc1cf0b686249a9fe0967"
HUGGINGFACE_API_KEY = "hf_6kVHkNy5qI0HffECA77eqml2gAwMHdOTV"
COHERE_API_KEY = "zHZN2IzWujeYvSp5DwphVbDRq2TPWxBJ8kqJ"


def call_llm(prompt, provider='openai'):
    endpoints = {
        "perplexity": "https://api.perplexity.com/v1/chat/completions",
        "xunfei": "https://api.xunfei.com/v1/chat/completions",
        "huggingface": "https://api.huggingface.com/v1/chat/completions",
        "cohere": "https://api.cohere.com/v1/chat/completions",
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
