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

            # --- Feu selon direction ---
            if vehicle.direction in ("EAST", "WEST"):
                light_state = self.traffic_light.ew_state
            else:
                light_state = self.traffic_light.ns_state

            # --- Sécurité distance ---
            too_close = False

            for other in self.vehicles:
                if other is vehicle:
                    continue

                if other.direction != vehicle.direction:
                    continue

                # Même voie → vérifier distance
                if vehicle.direction == "EAST" and 0 < other.xcor() - vehicle.xcor() < 30:
                    too_close = True
                elif vehicle.direction == "WEST" and 0 < vehicle.xcor() - other.xcor() < 30:
                    too_close = True
                elif vehicle.direction == "NORTH" and 0 < other.ycor() - vehicle.ycor() < 30:
                    too_close = True
                elif vehicle.direction == "SOUTH" and 0 < vehicle.ycor() - other.ycor() < 30:
                    too_close = True

            if too_close:
                vehicle.stop()
            else:
                self.scenario.apply_vehicle_behavior(vehicle, light_state)

            vehicle.move()

        