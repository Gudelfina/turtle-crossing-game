from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()

    def generate_car(self):
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            c = Turtle(shape="square")
            c.setheading(180)
            c.shapesize(stretch_wid=1, stretch_len=2)
            c.color(random.choice(COLORS))
            c.penup()
            c.goto(x=300, y=random.randint(-250, 250))
            self.all_cars.append(c)

    def move_car(self):
        for car in self.all_cars:
            car.fd(STARTING_MOVE_DISTANCE)
