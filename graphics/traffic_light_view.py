import turtle
from core.traffic_light import LightState

class TrafficLightView:
    def __init__(self, x=80, y=40):
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.turtle.penup()

        self.x = x
        self.y = y

        self.radius = 12
        self.off_color = "black"

    def draw_support(self):
        self.turtle.goto(self.x - 20, self.y + 50)
        self.turtle.color("black", "darkgray")
        self.turtle.begin_fill()
        for _ in range(2):
            self.turtle.forward(40)
            self.turtle.right(90)
            self.turtle.forward(140)
            self.turtle.right(90)
        self.turtle.end_fill()

    def draw_light(self, y_offset, color):
        self.turtle.goto(self.x, self.y - y_offset)
        self.turtle.color("black", color)
        self.turtle.begin_fill()
        self.turtle.circle(self.radius)
        self.turtle.end_fill()

    def draw(self, state: LightState):
        self.turtle.clear()
        self.draw_support()

        # Par défaut : lumières éteintes
        red = self.off_color
        orange = self.off_color
        green = self.off_color

        if state == LightState.RED:
            red = "red"
        elif state == LightState.ORANGE:
            orange = "orange"
        elif state == LightState.GREEN:
            green = "green"
        elif state == LightState.BLINK_ORANGE:
            orange = "orange"

        self.draw_light(20, red)
        self.draw_light(50, orange)
        self.draw_light(80, green)
