import turtle

class QuoridorX(Quoridor):
        def __init__(self):
            super().__init__()
        def square(self, yoda):
            yoda = turtle.Turtle()
            yoda.color("black")
            yoda.begin_fill()
            for x in range(4):
                yoda.forward(100)
                yoda.right(90)
            yoda.end_fill()