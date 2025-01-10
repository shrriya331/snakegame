from turtle import Turtle
import random

# defining the food class that creates the food for the snake
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        self.goto(x, y)
        self.refresh()

    def refresh(self):
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        self.goto(x, y)
