"""Load Topview API credentials for MCP and REST clients.

Priority order:
1. Environment variables TOPVIEW_UID + TOPVIEW_API_KEY
2. Credential file ~/.topview/credentials.json (set by auth.py login)
3. Error — prompts user to run auth.py login
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

CRED_FILE = Path.home() / ".topview" / "credentials.json"


def _load_from_file() -> dict | None:
    if not CRED_FILE.exists():
        return None
    try:
        data = json.loads(CRED_FILE.read_text())
        uid = str(data.get("uid", "")).strip()
        api_key = str(data.get("api_key", "")).strip()
        if uid and api_key:
            return {"uid": uid, "api_key": api_key}
    except (json.JSONDecodeError, OSError):
        pass
    return None


def load_config() -> dict:
    """Return a dict with uid and api_key, or exit with a helpful error message."""
    uid = os.environ.get("TOPVIEW_UID", "").strip()
    api_key = os.environ.get("TOPVIEW_API_KEY", "").strip()
    if uid and api_key:
        return {"uid": uid, "api_key": api_key}

    creds = _load_from_file()
    if creds:
        return creds

    print(
        "Error: Topview credentials not found.\n\n"
        "Option 1 — Log in (recommended):\n"
        "  python scripts/auth.py login\n\n"
        "Option 2 — Set environment variables:\n"
        '  export TOPVIEW_UID="<your-topview-uid>"\n'
        '  export TOPVIEW_API_KEY="<your-api-key>"\n',
        file=sys.stderr,
    )
    sys.exit(1)
