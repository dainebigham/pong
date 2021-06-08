from turtle import Turtle

ALIGN = 'center'
FONT = ('courier', 80, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=(FONT))