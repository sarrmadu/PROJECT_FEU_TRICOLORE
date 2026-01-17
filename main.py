from core.traffic_light import TrafficLight
from core.scenario import NormalTraffic
from core.simulation import Simulation
from graphics.scene import Scene
from graphics.traffic_light_view import TrafficLightView
from entities.vehicle import Vehicle
from ui.controls import Controls


def main():
    scene = Scene()
    traffic_light = TrafficLight()
    scenario = NormalTraffic()

    simulation = Simulation(traffic_light, scenario)

    vehicle = Vehicle()
    simulation.vehicles.append(vehicle)

    light_view = TrafficLightView()
    controls = Controls(simulation)
    controls.bind(scene.screen)

    simulation.start()

    while True:
        simulation.update()
        light_view.draw(traffic_light.state)
        scene.refresh()


if __name__ == "__main__":
    main()
