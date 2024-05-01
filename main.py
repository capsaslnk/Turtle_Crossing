import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

# Creating the environment for the game
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creation of the game items
player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

# Creating the user controls for game
screen.listen()
screen.onkey(player.move, "Up")

# Creation of the game logic
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_score()
        car_manager.level_up()

screen.exitonclick()
