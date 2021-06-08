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
        self.scoreboard()
        
    def scoreboard(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.l_score, align=ALIGN, font=(FONT))
        self.goto(100, 190)
        self.write(self.r_score, align=ALIGN, font=(FONT))

    def l_point(self):
        self.l_score += 1
        self.scoreboard()

    def r_point(self):
        self.r_score += 1
        self.scoreboard()