from pathlib import Path
import json

from socmini.ingest.windows_parser import parse_windows_security_logs
from socmini.detect.rule_loader import load_rules
from socmini.detect.engine import run_threshold_rule
from socmini.detect.alerts import create_alert

def main():
    raw_dir = Path("data/raw")
    normalized_dir = Path("data/normalized")
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    events = parse_windows_security_logs(raw_dir)

    rules = load_rules(Path("rules/windows"))

    alerts = []
    for rule in rules:
        matches = run_threshold_rule(events, rule)
        for m in matches:
            alerts.append(create_alert(m, rule))

    out_file = output_dir / "alerts.jsonl"
    with open(out_file, "w", encoding="utf-8") as f:
        for a in alerts:
            f.write(json.dumps(a) + "\n")

    print(f"[SOC-MINI] Generated {len(alerts)} alerts -> {out_file}")

if __name__ == "__main__":
    main()

