"""集成测试 - AI 平台连接"""
import os
import requests


class TestAIConnections:

    PERPLEXITY_KEY = "pplx-XroeQoG1fxWkdKp3LfNqM8Te19kLWIPM5Wf4X8nNdgfHex"

    def test_perplexity_connection(self):
        headers = {"Authorization": f"Bearer {self.PERPLEXITY_KEY}"}
        resp = requests.get("https://api.perplexity.com/v1/models", headers=headers)
        assert resp.status_code == 200

    FIREWORKS_KEY = "fw_dEOdkXcqJrm9X8LWZq9zuaYyvsn9J1Sr1"

    def test_fireworks_connection(self):
        headers = {"Authorization": f"Bearer {self.FIREWORKS_KEY}"}
        resp = requests.get("https://api.fireworks.com/v1/models", headers=headers)
        assert resp.status_code == 200

    SILICONFLOW_KEY = "sk-84TEUMD9U6Zh38HCp7XgskJ2zEtpgtWZ"

    def test_siliconflow_connection(self):
        headers = {"Authorization": f"Bearer {self.SILICONFLOW_KEY}"}
        resp = requests.get("https://api.siliconflow.com/v1/models", headers=headers)
        assert resp.status_code == 200

