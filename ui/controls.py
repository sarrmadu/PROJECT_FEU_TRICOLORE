class Controls:
    def __init__(self, simulation):
        self.simulation = simulation

    def bind(self, screen):
        screen.onkey(self.simulation.start, "s")
        screen.onkey(self.simulation.pause, "p")
        screen.onkey(self.simulation.reset, "r")
        screen.listen()
