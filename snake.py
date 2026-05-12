from turtle import Turtle
import time
import random
int_pos = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.game_on_state = True
        
    def create_snake(self):
        for position in int_pos:
            new_segment = Turtle("square") # Creates a brand new turtle each time
            new_segment.color("white")
            new_segment.penup()            # Stops it from drawing a line while moving
            new_segment.goto(position)     # Moves this specific turtle to its spot
            self.segments.append(new_segment)
    def move_forward(self):
         # Updates the screen to show the new positions of the segments
             # Pauses the program for a short amount of time (100 milliseconds)
            for seg_num in range(len(self.segments)-1, 0, -1): # Starts from the last segment and goes backwards
                new_x = self.segments[seg_num - 1].xcor() # Gets the x-coordinate of the segment in front
                new_y = self.segments[seg_num - 1].ycor() # Gets the y-coordinate of the segment in front
                self.segments[seg_num].goto(new_x, new_y)   # Moves the current segment to the position of the segment in front
            self.segments[0].forward(20)


    def up(self):
        self.segments[0].setheading(90) # Sets the direction of the head to up (90 degrees)

    def down(self):
        self.segments[0].setheading(270) # Sets the direction of the head to down (270 degrees)

    def left(self):
        self.segments[0].setheading(180) # Sets the direction of the head to left (180 degrees) 

    def right(self):
        self.segments[0].setheading(0) # Sets the direction of the head to right (0 degrees)

 
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Get the position of the last segment in the list
        self.add_segment(self.segments[-1].position())


    def wall_collision(self):
        head = self.segments[0]
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            self.game_on_state = False        




