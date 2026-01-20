import json
from pathlib import Path
from .normalize import normalize_event

def parse_windows_security_logs(path: Path):
    events = []

    for file in path.glob("*.json"):
        with open(file, "r", encoding="utf-8") as f:
            raw = json.load(f)

        event = normalize_event(
            ts=raw.get("TimeCreated"),
            host=raw.get("Computer"),
            user=raw.get("TargetUserName"),
            source_ip=raw.get("IpAddress"),
            event_type="auth",
            action="logon_failed" if raw.get("Status") != "0x0" else "logon_success",
            provider="windows_security",
            raw=raw,
        )

        events.append(event)

    return events
