from pathlib import Path
import json

from socmini.ingest.windows_parser import parse_windows_security_logs

def main():
    raw_dir = Path("data/raw")
    normalized_dir = Path("data/normalized")
    normalized_dir.mkdir(exist_ok=True)

    events = parse_windows_security_logs(raw_dir)

    out_file = normalized_dir / "events.jsonl"
    with open(out_file, "w", encoding="utf-8") as f:
        for e in events:
            f.write(json.dumps(e) + "\n")

    print(f"[SOC-MINI] Normalized {len(events)} events -> {out_file}")

if __name__ == "__main__":
    main()
