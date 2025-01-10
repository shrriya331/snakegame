# Importing modules
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# creating objects from classes
screen = Screen()
snake = Snake()
food = Food()
score = Scoreboard()

# Setting up the interface for the game
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

# assigning directions to keys of the keyboard
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# major functionality of the game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280  or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
