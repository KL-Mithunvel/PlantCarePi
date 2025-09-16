# mock_state_manager.py

import random
import time
from threading import Lock

# Internal simulated system state
_state = {
    "temp_c": 24.0,
    "rh": 55.0,
    "soil": 0.35,
    "lux": 300,
    "pump": False,
    "uv": False,
    "heater": False,
    "cooler": False,
    "fan": 0,
    "servo": 0
}

_state_lock = Lock()

def get_state():
    """Return a copy of the current system state."""
    with _state_lock:
        return _state.copy()

def update_fake_sensors():
    """Simulate sensor data changing over time."""
    with _state_lock:
        _state["temp_c"] += random.uniform(-0.2, 0.2)
        _state["rh"] += random.uniform(-0.5, 0.5)
        _state["soil"] += random.uniform(-0.01, 0.01)
        _state["lux"] = random.randint(250, 450)
        _state["temp_c"] = round(min(max(_state["temp_c"], 18), 35), 1)
        _state["rh"] = round(min(max(_state["rh"], 30), 90), 1)
        _state["soil"] = round(min(max(_state["soil"], 0.1), 0.6), 2)

def set_actuator(name, value):
    """Set state of an actuator."""
    with _state_lock:
        if name in _state:
            _state[name] = value
        else:
            raise KeyError(f"Unknown actuator: {name}")

def periodic_update(interval=1):
    """Run sensor update in background (optional for testing)."""
    try:
        while True:
            update_fake_sensors()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Stopped mock sensor simulation.")
