import time

from paddle import Paddle
from ball import Ball
from turtle import Screen
from time import sleep
from scoreboard import ScoreBoard
from ball import EDGE_OF_PLAY_FIELD_X

MAX_SCORE = 5


def set_up_screen_and_window():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("pong")
    screen.tracer(0)
    return screen


class PongGame:
    def __init__(self):
        self.screen = set_up_screen_and_window()
        self.left_paddle = Paddle((-350, 0))
        self.right_paddle = Paddle((350, 0))
        self.ball = Ball()
        self.screen.onkeypress(self.left_paddle.move_up, "w")
        self.screen.onkeypress(self.left_paddle.move_down, "s")
        self.screen.onkeypress(self.right_paddle.move_up, "Up")
        self.screen.onkeypress(self.right_paddle.move_down, "Down")
        self.screen.listen()
        self.scoreboard = ScoreBoard()

    def is_collision_happened_with_paddle(self):
        return self.ball.is_ball_touching_boundary_of_x() and (self.left_paddle.distance(self.ball.pos()) <= 50 or
                                                               self.right_paddle.distance(self.ball.pos()) <= 50)

    def play(self):
        game_is_on = True
        while game_is_on:
            sleep(self.ball.get_move_speed())
            if self.is_collision_happened_with_paddle():
                self.ball.setheading(self.ball.get_new_heading_after_paddle_bounce())
                self.ball.increase_speed()
            self.ball.move_the_ball()
            self.screen.update()
            game_is_on = self.ball.game_is_on()
            if not game_is_on:
                if self.ball.xcor() > EDGE_OF_PLAY_FIELD_X:
                    self.scoreboard.increase_score("left")
                elif self.ball.xcor() < -1 * EDGE_OF_PLAY_FIELD_X:
                    self.scoreboard.increase_score("right")
                if self.scoreboard.get_score("left") < MAX_SCORE and \
                        self.scoreboard.get_score("right") < MAX_SCORE:
                    self.ball.reset_ball()
                    game_is_on = True
                    time.sleep(1)
        self.screen.exitonclick()
