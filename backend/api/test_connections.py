"""集成测试 - AI 平台连接"""
import os
import requests


class TestAIConnections:

    XAI_KEY = "xai-cmmAjPazs8mfylJFQJq991rpHTqsoxqClrQYmOZb"

    def test_xai_connection(self):
        headers = {"Authorization": f"Bearer {self.XAI_KEY}"}
        resp = requests.get("https://api.xai.com/v1/models", headers=headers)
        assert resp.status_code == 200

    ALIYUN_KEY = "sk-dPyYPoB9lL3m4jo4V1bbTOd9qMq5F046"

    def test_aliyun_connection(self):
        headers = {"Authorization": f"Bearer {self.ALIYUN_KEY}"}
        resp = requests.get("https://api.aliyun.com/v1/models", headers=headers)
        assert resp.status_code == 200

    HUGGINGFACE_KEY = "hf_udWd7eoL32uNUu6qvmrPMHbQ8IpWOxgPF"

    def test_huggingface_connection(self):
        headers = {"Authorization": f"Bearer {self.HUGGINGFACE_KEY}"}
        resp = requests.get("https://api.huggingface.com/v1/models", headers=headers)
        assert resp.status_code == 200

