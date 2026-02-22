from backend.app.telemetry import log_event, telemetry_events


def test_log_event():
    initial = len(telemetry_events)
    evt = log_event('API_REQUEST', {'endpoint': '/prompts'})
    assert len(telemetry_events) == initial + 1
    assert evt['type'] == 'API_REQUEST'
