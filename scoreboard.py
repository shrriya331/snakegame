from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")

# updates the score and displays it on the interface
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.write(f"score: {self.score} high score: {self.high_score} ", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score} high score: {self.high_score}", align="center", font=("Courier", 24, "normal"))
        if self.score > self.high_score:
            self.high_score = self.score

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"score: {self.score} high score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    # def game_over(self):
    #
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=FONT)
