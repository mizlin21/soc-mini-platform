# SOC Mini Platform

## 5-Minute Demo (for recruiters & interviewers)

This repository demonstrates a complete SOC detection workflow:
from raw telemetry → normalized events → detections → alerts → triage → runbooks → validation.

**How to demo in 5 minutes:**
1. Run the pipeline to generate alerts
2. Open the alert output
3. Open the matching runbook
4. Show triage notes template
5. Show detection quality + tests

---

## Project summary
A mini SOC platform demonstrating:
- Log ingestion and normalization
- Detection engineering (MITRE mapped)
- Alerting and triage workflows
- Analyst runbooks
- Reproducible evidence for SOC interviews

> Status: Complete — SOC Mini Platform (case study)

## What this project demonstrates

**This project simulates a small but realistic Security Operations Center (SOC) workflow:**

- log ingestion and normalization
- detection engineering (rule-based, MITRE mapped)
- alert generation
- analyst triage workflows
- runbooks and investigation guidance
- detection quality documentation
- test-validated detection logic
- evidence artifacts for reproducibility

The goal is to demonstrate how raw telemetry becomes an actionable alert, and how analysts
make decisions after detection.

## Repository map (for reviewers)

- `src/socmini/` → ingestion, detection, alerting logic
- `rules/` → detection content (YAML rules)
- `runbooks/` → analyst investigation guidance
- `docs/` → detection quality, catalog, MITRE coverage
- `outputs/` → generated alerts
- `evidence/` → screenshots proving system behavior
- `tests/` → validation of detection logic

## Evidence

Screenshots proving system behavior are stored in `evidence/screenshots/`:
- alert generation
- raw log validation
- triage workflow
- detection quality and tests
- detection catalog and MITRE coverage
