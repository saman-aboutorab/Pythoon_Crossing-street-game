import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

path = 'C:\Users\Saman\Desktop\Code_Practice\data.txt'
screen = Screen()
screen.colormode(255)
screen.bgcolor(32, 42, 68)
screen.setup(width=600, height=600)

player = Player()

screen.tracer(0)

car_manager = CarManager()


screen.listen()
screen.onkey(player.move_forward, 'Up')
screen.onkey(player.move_backward, 'Down')
screen.onkey(player.move_left, 'Left')
screen.onkey(player.move_right, 'Right')

def check_collide():
    global game_is_on
    for number in range(len(car_manager.cars_list)):
        car = car_manager.cars_list[number]
        if abs(player.ycor() - car.ycor()) < 25:
            if abs(player.xcor() - car.xcor()) <= (car_manager.size[number] / 2 + 5):
                game_is_on = False

def read_highest_score():
    with open(path) as file:
        content = file.read()
        highest_score = int(content)
        print(highest_score)
        return highest_score


def check_record(level, highest_score):
    if level > highest_score:
        highest_score = level
        with open(path, 'w') as file:
            content = str(highest_score)
            print(content)
            file.write(content)


highest_score = read_highest_score()
timer = 0
level = 0
game_is_on = True

while game_is_on:
    timer += 0.1
    time.sleep(0.1)
    screen.update()
    car_manager.move_forward()
    car_manager.bring_back()
    check_collide()
    if player.ycor() > 250:
        player.reset()
        level += 1
        car_manager.levelup()
    if not game_is_on:
        check_record(level, highest_score)
        scoreboard = Scoreboard(level, highest_score)
        scoreboard.end_game()
        car_manager.color_black()
        screen.bgcolor('red')

screen.exitonclick()