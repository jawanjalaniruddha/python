import random

from braveturtle import BraveTurtle
from cars import Cars
from turtle import Screen
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

scoreboard = Scoreboard()
car = Cars()
braveturtle = BraveTurtle()
screen.listen()


game_is_on = True

while game_is_on:
    screen.onkeypress(braveturtle.move, "Up")
    time.sleep(0.1)
    # screen.update()

    car.create_car()
    car.move()

    for _ in car.all_cars:
        if braveturtle.distance(_) < 20:
            game_is_on = False
            scoreboard.game_over()

    if braveturtle.is_at_finish_line():
        braveturtle.go_to_start()
        car.level_up()
        scoreboard.score += 1
        scoreboard.update_score()


    screen.update()



screen.exitonclick()

# TODO: Make turtle to move up (Only up)
# TODO: Generate random cars and check for impact
# TODO: Increase levels if sucess and "Gamve over" if not. And keep score