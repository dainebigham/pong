from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pu()
        self.y_move = 10
        self.x_move = 10

    def move(self):
        y = self.ycor() + self.y_move
        x = self.xcor() + self.x_move
        self.goto(x, y)

    def bounce(self):
        self.y_move *= -1
        # self.x_move *= -1
