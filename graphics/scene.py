import turtle


class Scene:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(800, 400)
        self.screen.title("Simulation Feu Tricolore - Thiès")
        self.screen.tracer(0)

        self.drawer = turtle.Turtle()
        self.drawer.hideturtle()
        self.drawer.speed(0)
        self.drawer.color("gray")

        self.draw_crossroad()

    def draw_crossroad(self):
        self.drawer.penup()
        self.drawer.goto(-400, -40)
        self.drawer.pendown()
        self.drawer.begin_fill()

        # Route horizontale
        self.drawer.forward(800)
        self.drawer.left(90)
        self.drawer.forward(80)
        self.drawer.left(90)
        self.drawer.forward(800)
        self.drawer.left(90)
        self.drawer.forward(80)
        self.drawer.left(90)
        self.drawer.end_fill()

        # Route verticale
        self.drawer.penup()
        self.drawer.goto(-40, -200)
        self.drawer.pendown()
        self.drawer.begin_fill()
        self.drawer.left(90)
        self.drawer.forward(400)
        self.drawer.right(90)
        self.drawer.forward(80)
        self.drawer.right(90)
        self.drawer.forward(400)
        self.drawer.right(90)
        self.drawer.forward(80)
        self.drawer.end_fill()

    def refresh(self):
        self.screen.update()
