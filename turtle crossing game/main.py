import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

my_player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(my_player.move,"Up")
generation_count=0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if my_player.distance(car) <30:
            game_is_on=False
            my_player.write("Game Over!",align="center",font=("Courier",50,"normal"))

    if my_player.distance(0,280)<=15:
        my_player.restart_game()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()