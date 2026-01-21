import yaml
from pathlib import Path

def load_rules(path: Path):
    rules = []
    for file in path.glob("*.yaml"):
        with open(file, "r", encoding="utf-8") as f:
            rules.append(yaml.safe_load(f))
    return rules
