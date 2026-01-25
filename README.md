# SOC Mini Platform

A mini SOC platform demonstrating:
- Log ingestion and normalization
- Detection engineering (MITRE mapped)
- Alerting and triage workflows
- Analyst runbooks
- Reproducible evidence for SOC interviews

> Status: Day 0 – Skeleton and guardrails in place

## What this project demonstrates

This project simulates a small but realistic Security Operations Center (SOC) workflow:

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
