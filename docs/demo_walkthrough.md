
Paste **exactly this**:

```markdown
# SOC Mini Platform — Demo Walkthrough (5 minutes)

## 1. Problem
Raw logs are noisy. Alerts without context create fatigue.
This project shows how to turn telemetry into decisions.

---

## 2. Generate alerts
Run:

```powershell
$env:PYTHONPATH="src"
python -m socmini.cli
```

Open the alert output:
outputs/alerts.jsonl

---

## 3. Triage the alert
- Identify rule ID
- Open matching runbook
- Ask triage questions
- Assess risk
- Decide action

---

## 4. Validate detection quality
- Review detection_quality.md
- Show passing tests
- Discuss tuning decisions

---

## 5. Close
This system demonstrates how SOC analysts move from
events → signals → decisions → actions.