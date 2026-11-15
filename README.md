# agent学习 —— 从 0 开始

```
.env            真实配置（不进 git）
.env.example    模板
.gitignore      忽略 .env / .venv / workspace
main.py         读配置 → 调一次模型 → 打印回复
agent.py        只建 client，验证接入
pyproject.toml / uv.lock / .venv    uv 的环境
```

## 跑

```bash
uv sync
uv run main.py "你好"
```

## .env 怎么接入

默认用 python-dotenv（已 `uv add python-dotenv`）：

```python
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent / ".env")
client = OpenAI(api_key=os.environ["API_KEY"], base_url=os.environ["BASE_URL"])
```

也可以完全不写代码，让 uv 注入环境变量：

```bash
uv run --env-file .env main.py
```

换模型只改 `.env` 里的 `MODEL`；换 API 只改 `BASE_URL` 和 `API_KEY`。
临时覆盖（不改文件）：`MODEL=clef-oQ4e uv run main.py "你好"`。
