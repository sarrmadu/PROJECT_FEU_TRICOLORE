from enum import Enum
import time


class LightState(Enum):
    RED = "ROUGE"
    ORANGE = "ORANGE"
    GREEN = "VERT"
    BLINK_ORANGE = "ORANGE_CLIGNOTANT"


class TrafficLight:
    def __init__(self):
        self.state = LightState.RED
        self.manual_mode = False
        self.last_change = time.time()

    def change_state(self, new_state: LightState):
        self.state = new_state
        self.last_change = time.time()

    def next_state(self):
        if self.state == LightState.RED:
            return LightState.GREEN
        if self.state == LightState.GREEN:
            return LightState.ORANGE
        if self.state == LightState.ORANGE:
            return LightState.RED
        return self.state

    def update(self, durations: dict):
        if self.manual_mode or self.state == LightState.BLINK_ORANGE:
            return

        duration = durations.get(self.state)
        if duration is None:
            return

        if time.time() - self.last_change >= duration:
            self.change_state(self.next_state())
