from turtle import Turtle, Screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align = 'center', font = ("Arial",24,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align = 'center', font = ("Arial",24,"normal"))
        
    def r_point(self):
        self.update_scoreboard()
        self.r_score+=1
    
    def l_point(self):
        self.update_scoreboard()
        self.l_score+=1
