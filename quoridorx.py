import turtle


class QuoridorX(Quoridor):
    def __init__(self):
        super().__init__()
    
    def square(yoda, size):
        wn = turtle.Screen()
        yoda = turtle.Turtle()
        wn.bgcolor("white")
        yoda.color("black")
        yoda.speed(0)
        yoda.begin_fill()
        for i in range(4):
            yoda.forward(size)
            yoda.right(90)
        yoda.end_fill()
        yoda.penup()
        yoda.forward(size + 40)
        yoda.pendown()

    def ligne_damier(yoda, size):
        for i in range(10):
            square(yoda, size)
    
    def damier_complet(yoda, size, n):
        yoda.goto(4*(-size + 40), (size+40))

        for i in range(n):
            ligne_damier(yoda, size)
            yoda.backward(9*(size+40))
            yoda.right(90)

    def afficher_damier(self):
        damier_complet(yoda, 100)