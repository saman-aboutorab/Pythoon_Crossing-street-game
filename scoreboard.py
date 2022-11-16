from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self, level, highest_score):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.level = level
        self.highest_score = highest_score

    def end_game(self):
        self.penup()
        self.goto(0, 250)
        self.write(f"YOU LOST IN LEVEL {self.level}, THE HIGHEST SCORE IS {self.highest_score}", align='center', font=FONT)
