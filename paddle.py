from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('White')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x, y)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y <= 260:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y >= -240:
            self.goto(self.xcor(), new_y)
