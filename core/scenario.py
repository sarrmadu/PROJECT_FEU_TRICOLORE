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

        # --- Position et seuil selon direction ---
        if vehicle.direction == "EAST":
            pos = vehicle.xcor()
            approaching = pos < -40
        elif vehicle.direction == "WEST":
            pos = vehicle.xcor()
            approaching = pos > 40
        elif vehicle.direction == "NORTH":
            pos = vehicle.ycor()
            approaching = pos < -40
        else:  # SOUTH
            pos = vehicle.ycor()
            approaching = pos > 40

        # --- Comportement ---
        if light_state == LightState.RED and approaching:
            vehicle.stop()
        elif light_state == LightState.ORANGE and approaching:
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

        if vehicle.direction == "EAST":
            pos = vehicle.xcor()
            approaching = pos < -30
        elif vehicle.direction == "WEST":
            pos = vehicle.xcor()
            approaching = pos > 30
        elif vehicle.direction == "NORTH":
            pos = vehicle.ycor()
            approaching = pos < -30
        else:  # SOUTH
            pos = vehicle.ycor()
            approaching = pos > 30

        if light_state == LightState.RED and approaching:
            vehicle.stop()
        elif light_state == LightState.ORANGE and approaching:
            vehicle.slow_down()
        else:
            vehicle.go()



class NightTraffic(Scenario):
    def __init__(self):
        super().__init__("Mode nuit")

    def apply_vehicle_behavior(self, vehicle, light_state):
        vehicle.slow_down()
