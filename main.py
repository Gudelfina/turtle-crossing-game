import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.move_player, "Up")

game_is_on = True
while game_is_on:
    time.sleep(turtle.move_increment)
    screen.update()
    car.generate_car()
    car.move_car()

    # detect collision with car
    for cars in car.all_cars:
        if turtle.distance(cars) < 20:
            score.game_over()
            game_is_on = False

    if turtle.ycor() > 280:
        turtle.finish_line()
        score.level_up()


screen.exitonclick()
