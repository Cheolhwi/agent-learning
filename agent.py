"""最原始的版本：配置 → 客户端 → 调用

    uv run --env-file .env agent.py
"""
import os

from openai import OpenAI

# 1. 配置
BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:8010/v1")
API_KEY = os.environ.get("API_KEY", "cheolhwi")
MODEL = os.environ.get("MODEL", "Qwen3.8-Flash-Next-GSQ-RCO-Q2_0")

# 2. 客户端
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# 3. 调用
resp = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "你好"}],
)
print(resp.choices[0].message.content)
