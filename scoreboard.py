from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.setposition(-295, 280)
        self.hideturtle()
        self.score = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", move=False, align='left', font=('courier', 18, 'normal'))

    def game_over(self):
        self.clear()
        self.setposition(0, 0)
        self.write(f"Game Over!😞\n Your Score is {self.score}!", move=False, align='center', font=('courier', 18, 'normal'))
