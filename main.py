"""main.py —— 读 .env，调一次模型，打印回复

    uv run main.py "你好"
"""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent / ".env")

client = OpenAI(api_key=os.environ["API_KEY"], base_url=os.environ["BASE_URL"])
prompt = sys.argv[1] if len(sys.argv) > 1 else "你好"

resp = client.chat.completions.create(
    model=os.environ["MODEL"],
    messages=[{"role": "user", "content": prompt}],
)
print(resp.choices[0].message.content)
