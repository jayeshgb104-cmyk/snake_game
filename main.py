from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food


import time

screen = Screen()
screen.title("Snake Game")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

my_snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")
screen.update()
game_on_state = True

while game_on_state:
    screen.update()
    time.sleep(0.1)
    my_snake.move_forward()

    # Food Collision
    if my_snake.segments[0].distance(food) < 15:
        food.refresh()
        my_snake.extend()
        score_board.increase_score()

    # Wall Collision
    if abs(my_snake.segments[0].xcor()) > 290 or abs(my_snake.segments[0].ycor()) > 290:  
        score_board.reset()
        my_snake.reset_snake() # ADD THIS

    # Tail Collision
    for segment in my_snake.segments[1:]:
        if my_snake.segments[0].distance(segment) < 10:
            score_board.reset()
            my_snake.reset_snake() # ADD THIS




screen.exitonclick()