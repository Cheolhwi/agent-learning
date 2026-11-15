# agent学习 —— 从 0 开始

一个文件 `agent.py`：配置 → 客户端 → 调用。

```python
import os
from openai import OpenAI

BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:8010/v1")
API_KEY = os.environ.get("API_KEY", "cheolhwi")
MODEL = os.environ.get("MODEL", "Qwen3.8-Flash-Next-GSQ-RCO-Q2_0")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
resp = client.chat.completions.create(model=MODEL, messages=[{"role": "user", "content": "你好"}])
print(resp.choices[0].message.content)
```

## 环境变量从哪来

```bash
uv run --env-file .env agent.py     # uv 把 .env 注入进程，代码里不用读文件
export API_KEY=... && uv run agent.py
uv run agent.py                     # 没设环境时走代码里的默认值
```

## 文件

```
agent.py        唯一的代码
.env            真实配置（gitignore）
.env.example    模板
pyproject.toml  依赖（openai）
uv.lock / .venv uv 的环境
```
