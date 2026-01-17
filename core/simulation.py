class Simulation:
    def __init__(self, traffic_light, scenario):
        self.traffic_light = traffic_light
        self.scenario = scenario
        self.vehicles = []
        self.running = False
        self.paused = False

    def start(self):
        self.running = True
        self.paused = False

    def pause(self):
        self.paused = True

    def stop(self):
        self.running = False
        self.vehicles.clear()

    def reset(self):
        self.stop()
        self.traffic_light.change_state(self.traffic_light.state)

    def update(self):
        if not self.running or self.paused:
            return

        self.traffic_light.update(self.scenario.light_durations)

        for vehicle in self.vehicles:
            self.scenario.apply_vehicle_behavior(
                vehicle, self.traffic_light.state
            )
            vehicle.move()
