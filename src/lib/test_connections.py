"""集成测试 - AI 平台连接"""
import os
import requests


class TestAIConnections:

    VOLCANO_KEY = "b8d2296d-d5b8-4bfa-9b72-5c0926eeb92a"

    def test_volcano_connection(self):
        headers = {"Authorization": f"Bearer {self.VOLCANO_KEY}"}
        resp = requests.get("https://api.volcano.com/v1/models", headers=headers)
        assert resp.status_code == 200

    SILICONFLOW_KEY = "sk-4k05SvlalPtInko946hXe74vjjFaKBP0"

    def test_siliconflow_connection(self):
        headers = {"Authorization": f"Bearer {self.SILICONFLOW_KEY}"}
        resp = requests.get("https://api.siliconflow.com/v1/models", headers=headers)
        assert resp.status_code == 200

