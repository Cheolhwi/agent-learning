import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent / ".env")
client = OpenAI(api_key=os.environ["API_KEY"], base_url=os.environ["BASE_URL"])

models = [m.id for m in client.models.list()]
print("已接入:", os.environ["BASE_URL"], "| 模型数:", len(models))
print("当前 MODEL:", os.environ["MODEL"])
