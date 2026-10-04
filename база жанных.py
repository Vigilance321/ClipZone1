import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
USERS_FILE = DATA_DIR / "users.json"
VIDEOS_FILE = DATA_DIR / "videos.json"
COMMENTS_FILE = DATA_DIR / "comments.json"

def ensure_files():
    DATA_DIR.mkdir(exist_ok=True)
    for file_path in (USERS_FILE, VIDEOS_FILE, COMMENTS_FILE):
        if not file_path.exists():
            file_path.write_text("[]", encoding="utf-8")

def load_data(file_path):
    ensure_files()
    try:
        return json.loads(file_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []

def save_data(file_path, data):
    ensure_files()
    file_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=4),
        encoding="utf-8"
    )
