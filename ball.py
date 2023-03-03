from turtle import Turtle
import random

EDGE_OF_PLAY_FIELD_X = 320
EDGE_OF_PLAY_FIELD_Y = 280
STARTING_ANGLES = list(range(120, 151)) + list(range(210, 241)) + list(range(30, 61)) + list(range(300, 331))
STARTING_SPEED = 0.05


def choose_random_direction():
    return random.choice(STARTING_ANGLES)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setposition((0, 0))
        self.setheading(choose_random_direction())
        self.move_speed = STARTING_SPEED

    def increase_speed(self):
        self.move_speed *= 0.9

    def is_collision_happened(self):
        return self.ycor() >= EDGE_OF_PLAY_FIELD_Y or self.ycor() <= -1 * EDGE_OF_PLAY_FIELD_Y

    def get_new_heading_after_wall_bounce(self):
        return 360 - self.heading()

    def get_new_heading_after_paddle_bounce(self):
        return self.get_new_heading_after_wall_bounce() + 180

    def is_ball_touching_left_boundary_of_x(self):
        return self.xcor() <= -1*EDGE_OF_PLAY_FIELD_X

    def is_ball_touching_right_boundary_of_x(self):
        return self.xcor() >= EDGE_OF_PLAY_FIELD_X

    def is_ball_touching_boundary_of_x(self):
        return self.is_ball_touching_left_boundary_of_x() or self.is_ball_touching_right_boundary_of_x()

    def move_the_ball(self):
        if self.is_collision_happened():
            self.setheading(self.get_new_heading_after_wall_bounce())
        self.forward(10)

    def is_ball_over_left_boundary(self):
        return self.xcor() < -1 * EDGE_OF_PLAY_FIELD_X - 40

    def is_ball_over_right_boundary(self):
        return EDGE_OF_PLAY_FIELD_X + 40 < self.xcor()

    def game_is_on(self):
        return not self.is_ball_over_right_boundary() and not self.is_ball_over_left_boundary()

    def reset_ball(self):
        self.goto(0, 0)
        self.setheading(choose_random_direction())
        self.move_speed = STARTING_SPEED

    def get_move_speed(self):
        return self.move_speed
