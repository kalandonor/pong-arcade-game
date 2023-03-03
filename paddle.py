from turtle import Turtle
from scoreboard import ScoreBoard

EDGE_OF_PLAY_FIELD_Y = 250


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.goto(position)
        self.setheading(90)

    def move_up(self):
        if self.ycor() < EDGE_OF_PLAY_FIELD_Y:
            self.forward(20)

    def move_down(self):
        if self.ycor() > -1 * EDGE_OF_PLAY_FIELD_Y:
            self.backward(20)
