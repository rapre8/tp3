'''Permet de jouer en mode graphique (non terminé)'''
import turtle
from quoridor import Quoridor


class QuoridorX(Quoridor):
    '''Classe pour l'affichage graphique'''
    def __init__(self):
        super().__init__()

    def square(self, yoda, size):
        '''Permet de tracer le cadre'''
        wn = turtle.Screen()
        yoda = turtle.Turtle()
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
        '''Permet de tracer une ligne'''
        for _ in range(10):
            self.square(yoda, size)

    def damier_complet(self, yoda, size, n):
        '''Permet de tracer le damier complet'''
        yoda.goto(4*(-size + 40), (size+40))

        for _ in range(n):
            self.ligne_damier(yoda, size)
            yoda.backward(9*(size+40))
            yoda.right(90)

    def afficher_damier(self):
        '''Permet d'afficher le damier'''
        self.damier_complet('yoda', 100, 10)
