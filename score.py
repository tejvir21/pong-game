from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial',24,'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor('white')
        self.l_score = 0
        self.r_score = 0

    def score_display(self):
        self.clear()
        self.goto(100, 260)
        self.write(arg=f"[{self.r_score}]",align=ALIGN,font=FONT)
        self.goto(-100,260)
        self.write(arg=f"[{self.l_score}]",align=ALIGN,font=FONT)

    def update_l_score(self):
        self.l_score += 1

    def update_r_score(self):
        self.r_score += 1