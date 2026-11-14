"""env.py —— 把 .env 里的 KEY=VALUE 装进 os.environ（只用标准库）

接入方式：
    from env import load_dotenv
    load_dotenv()
    client = OpenAI(api_key=os.environ["API_KEY"], base_url=os.environ["BASE_URL"])
"""
import os
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parent / ".env"

def load_dotenv(path: Path = ENV_FILE) -> None:
    """逐行读 .env，写进环境变量；已经 export 的变量不会被覆盖"""
    if not path.exists():
        raise SystemExit(f"找不到 {path}，先执行:  cp .env.example .env")
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip(chr(34) + chr(39))   # 去掉首尾的 ' 或 "
        if key:
            os.environ.setdefault(key, value)
