from enum import Enum
import time

class LightState(Enum):
    RED = "ROUGE"
    ORANGE = "ORANGE"
    GREEN = "VERT"

class TrafficLight:
    def __init__(self):
        self.ns_state = LightState.RED      # Nord / Sud
        self.ew_state = LightState.GREEN   # Est / Ouest
        self.last_change = time.time()
        self.phase = "EW"  # EW ou NS

    def update(self, durations: dict):
        now = time.time()

        if self.phase == "EW":
            duration = durations.get(self.ew_state, 0)
            if now - self.last_change >= duration:
                self._next_ew()
        else:
            duration = durations.get(self.ns_state, 0)
            if now - self.last_change >= duration:
                self._next_ns()

    def _next_ew(self):
        if self.ew_state == LightState.GREEN:
            self.ew_state = LightState.ORANGE
        elif self.ew_state == LightState.ORANGE:
            self.ew_state = LightState.RED
            self.ns_state = LightState.GREEN
            self.phase = "NS"
        self.last_change = time.time()

    def _next_ns(self):
        if self.ns_state == LightState.GREEN:
            self.ns_state = LightState.ORANGE
        elif self.ns_state == LightState.ORANGE:
            self.ns_state = LightState.RED
            self.ew_state = LightState.GREEN
            self.phase = "EW"
        self.last_change = time.time()
