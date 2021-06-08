from turtle import Turtle

# initialise class and super
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.pu()
        self.goto(position)

    # find the current position of the paddle and then add 20 to the y axis
    # then move the paddle to that position on the y axis without moving in the x
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # as above, so below - but reverse
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)