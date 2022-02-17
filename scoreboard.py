from turtle import Turtle
FONT=("Courier", 60, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(0,200)
        self.p1_score = 0
        self.p2_score = 0
        self.show_current_score()

    def show_current_score(self):
        self.clear()
        self.write(f"{self.p2_score}    {self.p1_score}", align="center", font=FONT)

    def player1_scored(self):
        self.p1_score += 1

    def player2_scored(self):
        self.p2_score += 1