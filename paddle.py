from turtle import Turtle,Screen

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.goto(position)
    
    def go_up(self):
        y_cor = self.ycor()
        x_cor = self.xcor()
        y_cor +=20
        self.goto(x_cor,y_cor)

    def go_down(self):
        y_cor = self.ycor()
        x_cor = self.xcor()
        y_cor -=20
        self.goto(x_cor,y_cor)

        

