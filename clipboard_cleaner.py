import sys
import time
import json
import ctypes
from pathlib import Path

# -------- Config Path Handling --------

if getattr(sys, 'frozen', False):
    # Running as compiled EXE
    BASE_DIR = Path(sys.executable).parent
else:
    # Running as script
    BASE_DIR = Path(__file__).parent

CONFIG_FILE = BASE_DIR / "config.json"


def load_config():
    if not CONFIG_FILE.exists():
        return {"interval_seconds": 10}

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"interval_seconds": 10}


# -------- Clipboard Clear --------

def clear_clipboard():
    try:
        if ctypes.windll.user32.OpenClipboard(None):
            ctypes.windll.user32.EmptyClipboard()
            ctypes.windll.user32.CloseClipboard()
    except Exception:
        pass


# -------- Main Loop --------

def main():
    while True:
        config = load_config()  # reload each cycle so you can edit live
        interval = config.get("interval_seconds", 10)

        clear_clipboard()
        time.sleep(interval)


if __name__ == "__main__":
    main()
