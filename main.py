import turtle
import random
from core.traffic_light import TrafficLight
from core.scenario import NormalTraffic, RushHourTraffic, NightTraffic
from core.simulation import Simulation
from graphics.scene import Scene
from graphics.traffic_light_view import TrafficLightView
from entities.vehicle import Vehicle

# --- BOUTON MODERNE ---
class Button:
    def __init__(self, x, y, w, h, label, action, color="#00b4d8"):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.label = label
        self.color = color
        self.action = action
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.draw()

    def draw(self):
        self.t.goto(self.x, self.y)
        self.t.color("black", self.color)
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(self.w)
            self.t.right(90)
            self.t.forward(self.h)
            self.t.right(90)
        self.t.end_fill()
        self.t.goto(self.x + self.w/2, self.y - self.h + 10)
        self.t.color("white")
        self.t.write(self.label, align="center", font=("Arial", 12, "bold"))

    def is_clicked(self, x, y):
        return self.x <= x <= self.x + self.w and self.y - self.h <= y <= self.y

    def click(self):
        self.action()

# --- CONTROLS ---
class Controls:
    def __init__(self, simulation, scene):
        self.simulation = simulation
        self.scene = scene
        self.buttons = []
        self.create_buttons()
        self.scene.screen.onclick(self.handle_click)

    def create_buttons(self):
        UI_Y = 260  # position verticale des boutons (hors route)

        # --- Contrôle simulation ---
        self.buttons.append(Button(-360, UI_Y, 80, 35, "PLAY",
                                self.simulation.start, "#06d6a0"))  # vert
        self.buttons.append(Button(-270, UI_Y, 80, 35, "PAUSE",
                                self.simulation.pause, "#ffd166"))  # jaune
        self.buttons.append(Button(-180, UI_Y, 80, 35, "STOP",
                                self.simulation.stop, "#ef476f"))   # rouge
        self.buttons.append(Button(-90,  UI_Y, 80, 35, "RESET",
                                self.simulation.reset, "#118ab2"))  # bleu

        # --- Scénarios ---
        self.buttons.append(Button(30,  UI_Y, 100, 35, "Normal",
                                self.set_normal, "#2ec4b6"))        # vert clair
        self.buttons.append(Button(150, UI_Y, 100, 35, "Rush Hour",
                                self.set_rush, "#f77f00"))          # orange
        self.buttons.append(Button(270, UI_Y, 100, 35, "Night",
                                self.set_night, "#495057"))         # gris foncé

    def handle_click(self, x, y):
        for btn in self.buttons:
            if btn.is_clicked(x, y):
                btn.click()

    def set_normal(self):
        self.simulation.scenario = NormalTraffic()

    def set_rush(self):
        self.simulation.scenario = RushHourTraffic()

    def set_night(self):
        self.simulation.scenario = NightTraffic()

# --- VEHICULES COLORES ---
class ColoredVehicle(Vehicle):
    COLORS = ["blue", "red", "green", "orange", "purple"]

    def __init__(self):
        super().__init__()
        self.color(random.choice(self.COLORS))

# --- SCENE AMELIOREE ---
class StylishScene(Scene):
    def __init__(self):
        super().__init__()
        self.drawer.color("#555555")  # fond route gris
        self.draw_crossroad()
        self.draw_markings()

    def draw_markings(self):
        self.drawer.color("white")
        self.drawer.width(3)
        # horizontales
        for x in range(-380, 380, 40):
            self.drawer.penup()
            self.drawer.goto(x, 0)
            self.drawer.pendown()
            self.drawer.forward(20)
        # verticales
        for y in range(-180, 180, 40):
            self.drawer.penup()
            self.drawer.goto(0, y)
            self.drawer.setheading(90)
            self.drawer.pendown()
            self.drawer.forward(20)
        self.drawer.penup()

# --- MAIN ---
def main():
    scene = StylishScene()
    traffic_light = TrafficLight()
    scenario = NormalTraffic()
    simulation = Simulation(traffic_light, scenario)

    # Ajouter des véhicules
    for i in range(4):
        vehicle = ColoredVehicle()
        vehicle.goto(-300 - i*60, -20)
        simulation.vehicles.append(vehicle)

    controls = Controls(simulation, scene)

    simulation.start()
    # --- Feux tricolores sur chaque voie ---
    light_north = TrafficLightView(0, 100)
    light_south = TrafficLightView(0, -100)
    light_east  = TrafficLightView(100, 0)
    light_west  = TrafficLightView(-100, 0)

    light_views = [
        light_north,
        light_south,
        light_east,
        light_west
    ]


    # Boucle principale
    def update():
        simulation.update()
        light_north.draw(traffic_light.ns_state)
        light_south.draw(traffic_light.ns_state)

        light_east.draw(traffic_light.ew_state)
        light_west.draw(traffic_light.ew_state)

        
        scene.refresh()
        scene.screen.ontimer(update, 50)

    update()
    turtle.done()

if __name__ == "__main__":
    main()
