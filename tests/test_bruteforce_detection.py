from socmini.detect.engine import run_threshold_rule

def test_bruteforce_detection_fires():
    events = [
        {"event_type": "auth", "action": "logon_failed", "source_ip": "1.1.1.1"},
        {"event_type": "auth", "action": "logon_failed", "source_ip": "1.1.1.1"},
        {"event_type": "auth", "action": "logon_failed", "source_ip": "1.1.1.1"},
    ]

    rule = {
        "id": "SOC-WIN-T1110-001",
        "severity": "high",
        "logic": {
            "type": "threshold",
            "field": "source_ip",
            "match": {
                "event_type": "auth",
                "action": "logon_failed"
            },
            "threshold": 3
        },
        "description": "test"
    }

    matches = run_threshold_rule(events, rule)
    assert len(matches) == 1
