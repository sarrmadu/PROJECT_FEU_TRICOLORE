# --- Simulation.py ---
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
        # ne pas vider les véhicules pour pouvoir relancer

    def reset(self):
        self.traffic_light.change_state(self.traffic_light.state.RED)
        for v in self.vehicles:
            v.goto(-300, -20)
            v.go()
        self.running = False
        self.paused = False

    def change_scenario(self, new_scenario):
        self.scenario = new_scenario
        self.traffic_light.last_change = 0  # pour que les nouvelles durées prennent effet immédiatement


    def update(self):
        if not self.running or self.paused:
            return
        self.traffic_light.update(self.scenario.light_durations)
        for vehicle in self.vehicles:
            # Choisir le bon feu selon la direction
            if vehicle.direction in ("EAST", "WEST"):
                light_state = self.traffic_light.ew_state
            else:  # NORTH / SOUTH
                light_state = self.traffic_light.ns_state

            self.scenario.apply_vehicle_behavior(vehicle, light_state)
            vehicle.move()

    