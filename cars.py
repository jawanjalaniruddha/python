import random
from turtle import Turtle, Screen

color_list = ["red", "green", "blue", "yellow", "pink", "red", "magenta", "green", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 15

class Cars(Turtle):
    def __init__(self):
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 5

    def create_car(self):
        # super(Cars, self).__init__()
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(color_list))
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
        # self.forward(random.randint(5, 20))

    def level_up(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT
