from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    """Creating the scoreboard class"""

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Method for updating the score"""
        self.goto(0, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def increase_score(self):
        """Method for increasing the score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """Method for printing game over"""
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            move=False,
            align="center",
            font=("Courier", 24, "bold"),
        )
