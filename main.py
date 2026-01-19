from core.traffic_light import TrafficLight
from core.scenario import NormalTraffic
from core.simulation import Simulation
from graphics.scene import Scene
from graphics.traffic_light_view import TrafficLightView
from entities.vehicle import Vehicle
import turtle

# --- CLASSE BOUTON ---
class Button:
    def __init__(self, x, y, w, h, label, action):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.action = action

        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.draw(label)

    def draw(self, label):
        self.t.goto(self.x, self.y)
        self.t.color("black", "lightgray")
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(self.w)
            self.t.right(90)
            self.t.forward(self.h)
            self.t.right(90)
        self.t.end_fill()
        self.t.goto(self.x + self.w/2, self.y - self.h + 8)
        self.t.write(label, align="center", font=("Arial", 10, "bold"))

    def is_clicked(self, x, y):
        return (self.x <= x <= self.x + self.w) and (self.y - self.h <= y <= self.y)

    def click(self):
        self.action()

# --- CONTROLES AVEC BOUTONS ---
class Controls:
    def __init__(self, simulation, scene):
        self.simulation = simulation
        self.scene = scene
        self.buttons = []
        self.create_buttons()
        self.scene.screen.onclick(self.handle_click)

    def create_buttons(self):
        self.buttons.append(Button(-360, 180, 70, 30, "PLAY", self.simulation.start))
        self.buttons.append(Button(-280, 180, 70, 30, "PAUSE", self.simulation.pause))
        self.buttons.append(Button(-200, 180, 70, 30, "STOP", self.simulation.stop))
        self.buttons.append(Button(-120, 180, 70, 30, "RESET", self.simulation.reset))

    def handle_click(self, x, y):
        for btn in self.buttons:
            if btn.is_clicked(x, y):
                btn.click()


# --- MAIN ---
def main():
    scene = Scene()
    traffic_light = TrafficLight()
    scenario = NormalTraffic()
    simulation = Simulation(traffic_light, scenario)

    # Ajouter des véhicules
    for _ in range(3):
        vehicle = Vehicle()
        simulation.vehicles.append(vehicle)

    light_view = TrafficLightView()
    controls = Controls(simulation, scene)

    simulation.start()

    # Boucle principale
    def update():
        simulation.update()
        light_view.draw(traffic_light.state)
        scene.refresh()
        scene.screen.ontimer(update, 50)

    update()
    turtle.done()


if __name__ == "__main__":
    main()
