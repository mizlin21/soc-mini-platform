# Detection Quality & Tuning Notes

This document records known false positives, tuning guidance, and quality considerations
for detections in the SOC Mini Platform.

---

## Detection: SOC-WIN-T1110-001 (Brute Force - Windows)

### What it detects well
- repeated failed logons from one source IP
- external brute force attempts
- noisy password guessing behavior

### Known false positives
- misconfigured scheduled tasks
- service accounts with expired passwords
- vulnerability scanners
- users repeatedly mistyping passwords

### Recommended tuning
- increase threshold from 3 → 5 for internal networks
- exclude known scanner IPs
- exclude known service accounts
- lower threshold for privileged accounts

### Confidence level
Medium–High (requires context for escalation)

---

## General quality principles
- Prefer behavior over single events
- Use thresholds to reduce noise
- Always document exclusions
- Never tune blindly without evidence

## Evidence
See `evidence/screenshots/` for alert output and triage workflow showing
detection behavior and analyst decision process.
