import turtle


class Vehicle(turtle.Turtle):
    def __init__(self, x=-300, y=-20):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.goto(x, y)
        self.speed_value = 2

    def move(self):
        self.forward(self.speed_value)

        if self.xcor() > 350:
            self.goto(-350, self.ycor())

    def stop(self):
        self.speed_value = 0

    def slow_down(self):
        self.speed_value = 1

    def go(self):
        self.speed_value = 2
