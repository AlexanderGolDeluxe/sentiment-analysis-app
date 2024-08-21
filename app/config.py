from pathlib import Path

from environs import Env
from loguru import logger

ENV = Env(expand_vars=True)
ENV.read_env()

BASE_DIR = Path(__file__).parent.parent
DEBUG_MODE = ENV.bool("DEBUG_MODE")
HF_API_TOKEN = ENV.str("HF_API_TOKEN")
HF_MODEL_NAME = ENV.str("HF_MODEL_NAME")
DB_URL = (
    Path(f"{BASE_DIR}/app/db").mkdir(parents=True, exist_ok=True) or
    f"sqlite+aiosqlite:///{BASE_DIR}/app/db/{BASE_DIR.stem}.sqlite3"
)

logger.add(
    f"{BASE_DIR}/app/logs/{BASE_DIR.stem}_app.log",
    format="{time} {level} {message}",
    level="DEBUG",
    rotation="1 day",
    retention="7 days")
