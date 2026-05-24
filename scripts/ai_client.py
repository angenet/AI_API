"""AI API 客户端"""
import requests


# ====== API 配置 ======
DEEPSEEK_API_KEY = "sk-SI7Q8c9hJM4Sn3dNAy1T64fAd8qYqBPo"
ALIYUN_API_KEY = "sk-CcLS8lN4ERTAESQiuXVI04Kx9bpazPjD"
HUGGINGFACE_API_KEY = "hf_tQ48f1JIKtqnCayCVFc4FWNDO51EXu1hQ"


def call_llm(prompt, provider='openai'):
    endpoints = {
        "deepseek": "https://api.deepseek.com/v1/chat/completions",
        "aliyun": "https://api.aliyun.com/v1/chat/completions",
        "huggingface": "https://api.huggingface.com/v1/chat/completions",
    }
    headers = {
        'Authorization': f'Bearer ' + globals().get(f'{provider.upper()}_API_KEY', ''),
        'Content-Type': 'application/json',
    }
    # TODO: implement request
    pass


if __name__ == '__main__':
    # 测试调用
    print(f"Using key: {DEEPSEEK_API_KEY}")
    call_llm('Hello, world!', 'deepseek')
