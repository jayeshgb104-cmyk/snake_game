from turtle import Screen
import scoreboard
from snake import Snake
from food import Food
from scoreboard import Scoreboard

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
     # In main.py loop:
     # Inside while game_on_state:
     if my_snake.segments[0].distance(food) < 15:
        food.refresh() # This will now work correctly!
        my_snake.extend() # This will now work correctly!
        score_board.increase_score() # This will now work correctly!
     my_snake.wall_collision()
     
    # 3. Check if we should stop the game
     if my_snake.game_on_state == False:
        game_on_state = False
        score_board.game_over()

     for segment in my_snake.segments[1:]:
        if my_snake.segments[0] == segment:
            pass
        elif my_snake.segments[0].distance(segment) < 10:
            game_on_state = False
            score_board.game_over()   



screen.exitonclick()