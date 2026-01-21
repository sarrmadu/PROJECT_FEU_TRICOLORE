import turtle
from core.traffic_light import LightState

class TrafficLightView:
    def __init__(self, x=40, y=40):
        self.x = x
        self.y = y
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.t.speed(0)
        self.t.width(2)

    def draw(self, state: LightState):
        self.t.clear()

        # ─── BOITIER ───
        self.t.goto(self.x - 18, self.y + 50)
        self.t.setheading(0)
        self.t.color("black", "#444444")
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(36)
            self.t.right(90)
            self.t.forward(100)
            self.t.right(90)
        self.t.end_fill()

        # ─── FEUX ───
        self._draw_light(self.y + 30, state == LightState.RED, "red")
        self._draw_light(self.y,      state == LightState.ORANGE, "orange")
        self._draw_light(self.y - 30,  state == LightState.GREEN, "green")

    def _draw_light(self, y, active, color):
        self.t.goto(self.x, y)
        self.t.setheading(0)
        self.t.penup()

        if active:
            self.t.color(color)
        else:
            self.t.color("#111111")

        self.t.dot(20)
