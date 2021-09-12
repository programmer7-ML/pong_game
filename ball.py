from turtle import Turtle, Screen

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def change_position(self):
        x1 = self.xcor() + self.x_move
        y1 = self.ycor() + self.y_move
        self.goto(x1,y1)
    
    def bounce_y(self):
        self.y_move *=-1
    
    def bounce_x(self):
        self.x_move *=-1
    
    def reset(self):
        self.goto(0,0)
        self.bounce_x()


