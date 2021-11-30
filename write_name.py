from turtle import Turtle
TEXT_FONT = ('Courier', 8, 'normal')


class WriteName (Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('black')

    def write_on_screen(self, text, x_coordinate, y_coordinate):
        self.goto(x_coordinate, y_coordinate)
        # self.write(arg=text, move=False, align='left', font=TEXT_FONT)
        self.write(text)
