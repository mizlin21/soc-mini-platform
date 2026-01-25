# SOC Mini Platform Architecture

Raw Logs (JSON)
     |
     v
Ingest & Normalize
     |
     v
Normalized Events (JSONL)
     |
     v
Detection Engine (rules)
     |
     v
Alerts (JSONL)
     |
     v
Analyst Workflow
  ├─ Runbooks
  ├─ Triage Notes
  ├─ Tuning & Quality Notes
  └─ Tests (detection validation)
