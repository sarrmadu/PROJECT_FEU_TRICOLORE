import turtle


class Vehicle(turtle.Turtle):
    def __init__(self, direction="EAST"):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()

        self.direction = direction
        self.speed_value = 2

        # Position initiale selon la direction
        if direction == "EAST":      # gauche → droite
            self.goto(-350, -20)
            self.setheading(0)
        elif direction == "WEST":    # droite → gauche
            self.goto(350, 20)
            self.setheading(180)
        elif direction == "NORTH":   # bas → haut
            self.goto(20, -350)
            self.setheading(90)
        elif direction == "SOUTH":   # haut → bas
            self.goto(-20, 350)
            self.setheading(270)

    def move(self):
        self.forward(self.speed_value)

        # Réapparition
        if abs(self.xcor()) > 380 or abs(self.ycor()) > 380:
            self.reset_position()

    def reset_position(self):
        if self.direction == "EAST":
            self.goto(-350, -20)
        elif self.direction == "WEST":
            self.goto(350, 20)
        elif self.direction == "NORTH":
            self.goto(20, -350)
        elif self.direction == "SOUTH":
            self.goto(-20, 350)

    def stop(self):
        self.speed_value = 0

    def slow_down(self):
        self.speed_value = 1

    def go(self):
        self.speed_value = 2
