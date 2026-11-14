# agent学习 —— 从 0 开始

只有两个文件要理解：`.env` 和 `env.py`。

```
.env            真实配置（不进 git）
.env.example    模板
.gitignore      忽略 .env / .venv / workspace
env.py          读 .env → 装进 os.environ
main.py         读配置 → 调一次模型 → 打印回复
pyproject.toml / uv.lock / .venv    uv 的环境
```

## 跑

```bash
uv sync
uv run main.py "你好"
```

## 接入 .env 的三行

```python
import os
from env import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.environ["API_KEY"], base_url=os.environ["BASE_URL"])
```

换模型只改 `.env` 里的 `MODEL`；换 API 只改 `BASE_URL` 和 `API_KEY`。
临时覆盖（不改文件）：`MODEL=clef-oQ4e uv run main.py "你好"`。
