from turtle import Turtle

# initialise class and super
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pu()
        # movement variables
        self.y_move = 10
        self.x_move = 10

    # find the current x and y position of the ball and add the values of the movement variables respectively
    # then move the ball to the updated x and y position
    def move(self):
        y = self.ycor() + self.y_move
        x = self.xcor() + self.x_move
        self.goto(x, y)

    # if the ball hits the top or bottom of the screen, multiply the y value by -1 to reverse direction
    def bounce_y(self):
        self.y_move *= -1

    # as above, so below - but for the x axis
    def bounce_x(self):
        self.x_move *= -1

    # send ball back to centre of the screen and reverse the direction along the x axis
    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        