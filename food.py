from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__() # This creates the turtle
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) 
        self.color("red")
        self.speed("fastest")
        self.refresh()

    # In food.py refresh() method
    def refresh(self):
        # Use a smaller range (e.g., 270) to stay safely away from the 290 wall
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)

