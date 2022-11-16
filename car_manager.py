import random
from turtle import Turtle
COUNT = 15
BASE_SPEED = 3

class CarManager:

    def __init__(self):
        self.stretch_list = []
        self.cars_list = []
        self.speed_list = []
        self.size = []
        self.create_cars()
        self.create_speed()
        self.measure()

    def create_speed(self):
        self.speed_list = []
        for car in range(COUNT):
            self.speed_list.append(BASE_SPEED + random.randint(-5, 5))

    def change_color(self, car):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        car.color(r, g, b)

    def create_cars(self):
        for car in range(COUNT):
            new_car = Turtle()
            new_car.shape('square')
            stretch = 1 + random.random() * 3
            self.stretch_list.append(stretch)
            new_car.shapesize(1, stretch)
            new_car.penup()
            x = random.randint(-15, 15) * 20
            y = random.randint(-12, 12) * 20
            new_car.goto(x, y)
            self.change_color(new_car)
            self.cars_list.append(new_car)
        print(self.stretch_list)

    def move_forward(self):
        for car in range(COUNT):
            self.cars_list[car].forward(self.speed_list[car])


    def bring_back(self):
        for car in range(COUNT):
            x = self.cars_list[car].xcor()
            y = self.cars_list[car].ycor()
            if x > 330:
                new_x = x - 630
                self.cars_list[car].goto(new_x, y)
            if x < -330:
                new_x = x + 630
                self.cars_list[car].goto(new_x, y)

    def measure(self):
        for car in range(COUNT):
            self.size.append(self.stretch_list[car] * 20)

    def color_black(self):
        for car in self.cars_list:
            car.color('black')

    def levelup(self):
        global BASE_SPEED
        BASE_SPEED += 2
        self.create_speed()