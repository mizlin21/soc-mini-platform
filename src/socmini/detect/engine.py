from collections import defaultdict

def run_threshold_rule(events, rule):
    counts = defaultdict(int)
    matches = []

    for e in events:
        if (
            e["event_type"] == rule["logic"]["match"]["event_type"]
            and e["action"] == rule["logic"]["match"]["action"]
        ):
            key = e.get(rule["logic"]["field"])
            counts[key] += 1
            if counts[key] == rule["logic"]["threshold"]:
                matches.append({
                    "rule_id": rule["id"],
                    "severity": rule["severity"],
                    "source_ip": key,
                    "count": counts[key],
                    "description": rule["description"],
                })

    return matches
