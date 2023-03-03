from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    def increase_score(self, player=None):
        if player == "left":
            self.left_score += 1
        elif player == "right":
            self.right_score += 1
        self.update_scoreboard()

    def get_score(self, player):
        if player == "left":
            return self.left_score
        return self.right_score
