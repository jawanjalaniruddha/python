import random
from turtle import Turtle, Screen


screen = Screen()
colors = ["red", "orange", "blue", "yellow", "green", "magenta"]
all_turtles = []


is_race_on = False
y_cor = 150
x_cor = -200

user_bet = screen.textinput(title="Make your bet", prompt="What color turtle you want to the race? Enter the color")

if user_bet in colors:
    is_race_on = True

screen.setup(width=500, height=400)
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.circle(10)
    new_turtle.goto(x=x_cor, y=y_cor)
    all_turtles.append(new_turtle)
    y_cor -= 50

while is_race_on:
    for turtle in all_turtles:
        rand_distances = random.randint(1, 10)
        turtle.forward(rand_distances)
        x = turtle.xcor()
        if x > 230:
            is_race_on = False
            if turtle.color()[0] == user_bet:
                print(f"You've won! The {user_bet} turtle has won the race!")
            else:
                print(f"You've lost! The {turtle.color()[0]} turtle has won the race!")
                is_race_on = False










screen.exitonclick()
