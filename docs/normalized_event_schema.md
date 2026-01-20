# Normalized Event Schema (v1)

This schema defines the contract for all telemetry entering the SOC Mini Platform.
All parsers MUST emit events in this format.

## Required Fields

| Field | Type | Description |
|------|------|-------------|
| ts | string (ISO8601) | Event timestamp |
| host | string | Hostname where event occurred |
| user | string | Username involved |
| source_ip | string | Source IP address |
| event_type | string | auth, process, network, file |
| action | string | Specific action (logon_failed, process_start, connection_attempt) |
| process_name | string | Executable name (if applicable) |
| command_line | string | Full command line (if applicable) |
| destination_ip | string | Destination IP (network events) |
| destination_port | int | Destination port (network events) |
| provider | string | Log source (windows_security, linux_auth, zeek, etc.) |
| raw | object | Original raw event payload |

## Optional Fields
- parent_process
- logon_type
- status
- severity_hint

## Design Principles
- Every event must be self-contained
- Missing fields use null
- Never drop raw data
- Detection logic must rely on normalized fields, not raw
