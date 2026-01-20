from datetime import datetime

def normalize_event(
    ts,
    host,
    user,
    source_ip,
    event_type,
    action,
    provider,
    raw,
    process_name=None,
    command_line=None,
    destination_ip=None,
    destination_port=None,
):
    return {
        "ts": ts or datetime.utcnow().isoformat(),
        "host": host,
        "user": user,
        "source_ip": source_ip,
        "event_type": event_type,
        "action": action,
        "process_name": process_name,
        "command_line": command_line,
        "destination_ip": destination_ip,
        "destination_port": destination_port,
        "provider": provider,
        "raw": raw,
    }
