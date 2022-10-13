from turtle import Turtle, Screen
import random
from tkinter import *
import heroes
sammy = Turtle()
sammy.shape("turtle")
sammy.color("red")

shape = ["triangle", "square", "pentagon","hexagon", "heptagon", "octagon", "nonagon", "decagon"]


def random_color():
    return random.randint(0,0x1000000)


# def draw_shape():
#     for each_num in range(3, 11):
#         color = "#" + '{:06x}'.format(random_color())
#         angle = 360 / each_num
#         print(angle)
#         print(each_num)
#         for i in range(each_num):
#
#             sammy.color(color)
#             sammy.forward(100)
#             sammy.left(angle)
#
#
# draw_shape()

def draw_shape(num):
    angle = 360 / num
    for i in range(num):
        sammy.forward(100)
        sammy.left(angle)


for each_num in range(3, 11):
    color = "#" + '{:06x}'.format(random_color())
    sammy.color(color)
    draw_shape(each_num)

screen = Screen()
screen.exitonclick()