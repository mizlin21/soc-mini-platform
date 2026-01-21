from datetime import datetime

def create_alert(match, rule):
    return {
        "alert_id": f"{rule['id']}-{datetime.utcnow().isoformat()}",
        "rule_id": rule["id"],
        "name": rule["name"],
        "severity": rule["severity"],
        "description": rule["description"],
        "source_ip": match.get("source_ip"),
        "count": match.get("count"),
        "created_at": datetime.utcnow().isoformat()
    }
