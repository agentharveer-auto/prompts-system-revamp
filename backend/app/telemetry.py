from datetime import datetime

# Simple in-memory telemetry store for MVP
telemetry_events = []

def log_event(event_type: str, details: dict):
    evt = {
        "event_id": str(__import__('uuid').uuid4()),
        "type": event_type,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "details": details
    }
    telemetry_events.append(evt)
    return evt
