from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
HEADING = 90
FORWARD = 10
FINISH_LINE_Y = 280


class BraveTurtle(Turtle):
    def __init__(self):
        super(BraveTurtle, self).__init__()
        self.penup()
        self.go_to_start()
        self.color("black")
        self.shape("turtle")
        self.setheading(HEADING)

    def move(self):
        if self.ycor() < 290:
            self.forward(FORWARD)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

