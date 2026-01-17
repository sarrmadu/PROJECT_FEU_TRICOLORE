from core.traffic_light import LightState


class Scenario:
    def __init__(self, name):
        self.name = name
        self.light_durations = {}

    def apply_vehicle_behavior(self, vehicle, light_state):
        raise NotImplementedError


class NormalTraffic(Scenario):
    def __init__(self):
        super().__init__("Circulation normale")
        self.light_durations = {
            LightState.RED: 4,
            LightState.GREEN: 5,
            LightState.ORANGE: 2
        }

    def apply_vehicle_behavior(self, vehicle, light_state):
        if light_state == LightState.RED and vehicle.xcor() < -40:
            vehicle.stop()
        elif light_state == LightState.ORANGE and vehicle.xcor() < -40:
            vehicle.slow_down()
        else:
            vehicle.go()


class RushHourTraffic(Scenario):
    def __init__(self):
        super().__init__("Heure de pointe")
        self.light_durations = {
            LightState.RED: 3,
            LightState.GREEN: 7,
            LightState.ORANGE: 1
        }

    def apply_vehicle_behavior(self, vehicle, light_state):
        if light_state == LightState.RED and vehicle.xcor() < -30:
            vehicle.stop()
        elif light_state == LightState.ORANGE and vehicle.xcor() < -30:
            vehicle.slow_down()
        else:
            vehicle.go()


class NightTraffic(Scenario):
    def __init__(self):
        super().__init__("Mode nuit")

    def apply_vehicle_behavior(self, vehicle, light_state):
        vehicle.slow_down()
