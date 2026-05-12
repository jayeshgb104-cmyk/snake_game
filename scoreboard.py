from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        
        # 1. Read the saved high score from the file when the game starts
        try:
            with open("data.txt", mode="r") as data:
                self.high_score = int(data.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0 # If file doesn't exist, start at 0
            
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                    data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

