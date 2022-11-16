from turtle import Turtle
import random



STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('white')
        self.reset()
        self.setheading(90)

    def reset(self):
        self.goto(STARTING_POSITION)

    def move_forward(self):
        x = self.xcor()
        y = self.ycor()
        new_y = y + MOVE_DISTANCE
        self.goto(x, new_y)

    def move_backward(self):
        x = self.xcor()
        y = self.ycor()
        new_y = y - MOVE_DISTANCE
        self.goto(x, new_y)

    def move_left(self):
        x = self.xcor()
        y = self.ycor()
        new_x = x - MOVE_DISTANCE
        self.goto(new_x, y)

    def move_right(self):
        x = self.xcor()
        y = self.ycor()
        new_x = x + MOVE_DISTANCE
        self.goto(new_x, y)