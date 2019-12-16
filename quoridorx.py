import turtle
from quoridor import Quoridor, QuoridorError


class QuoridorX(Quoridor):
    def __init__(self):
        super().__init__()
    
    def square(self, yoda, size):
        wn = turtle.Screen()
        self.yoda = turtle.Turtle()
        wn.bgcolor("white")
        yoda.color("black")
        yoda.speed(0)
        yoda.begin_fill()
        for _ in range(4):
            yoda.forward(size)
            yoda.right(90)
        yoda.end_fill()
        yoda.penup()
        yoda.forward(size + 40)
        yoda.pendown()

    def ligne_damier(self, yoda, size):
        for _ in range(10):
            self.square(yoda, size)
    
    def damier_complet(self, yoda, size, n):
        yoda.goto(4*(-size + 40), (size+40))

        for _ in range(n):
            self.ligne_damier(yoda, size)
            yoda.backward(9*(size+40))
            yoda.right(90)

    def afficher_damier(self):
        self.damier_complet(self.yoda, 100, 10)