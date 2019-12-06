import random
from itertools import product
import networkx as nx
import turtle
from quoridor import Quoridor, QuoridorError


class QuoridorX(Quoridor):
    def __init__(self, joueurs, murs=None):
        self.joueur1 = joueurs[0]
        self.joueur2 = joueurs[1]
        self.murs = murs
        if str(self.joueur1) == self.joueur1:
            self.gamestate = {'joueurs':
                            [{'nom': self.joueur1, 'murs': 10, 'pos': [5, 1]},
                             {'nom': self.joueur2, 'murs': 10, 'pos': [5, 9]}],
                              'murs': {'horizontaux': [], 'verticaux': []}}
        else:
            self.gamestate = {'joueurs':
                            [self.joueur1, self.joueur2],
                              'murs': {'horizontaux': [], 'verticaux': []}}

        if isinstance(self.murs, dict):
            self.gamestate['murs'] = self.murs

            for i in murs['verticaux']:
                if i[0] < 2 or i[1] > 8:
                    raise QuoridorError("Position mur vertical invalide")
                if i not in list(product(range(1, 10), repeat=2)):
                    raise QuoridorError("Position mur vertical invalide")

            for i in murs['horizontaux']:
                if i[0] > 8 or i[1] < 2:
                    raise QuoridorError("Position mur horizontal invalide")
                if i not in list(product(range(1, 10), repeat=2)):
                    raise QuoridorError("Position mur horizontal invalide")

            murs_dispos = joueurs[0].get('murs') + joueurs[1].get('murs')
            murs_placés = len(murs['horizontaux']) + len(murs['verticaux'])
            if murs_dispos + murs_placés != 20:
                raise QuoridorError("Le total des murs placés et plaçables n'est pas égal à 20")

        else:
            if self.murs is not None:
                raise QuoridorError("L'argument murs n'est pas un dictionnaire")

        if isinstance(joueurs[0], dict):
            for i in range(2):
                if joueurs[i]['murs'] < 0 or joueurs[i]['murs'] > 10:
                    raise QuoridorError("Nombre de murs qu'un joueur peut placer invalide")

            for i in range(2):
                if joueurs[i]['pos'] not in list(product(range(1, 10), repeat=2)):
                    raise QuoridorError("Position du joueur invalide")

            if murs is None:
                if joueurs[0]['murs'] + joueurs[1]['murs'] != 20:
                    raise QuoridorError("Le total des murs placés et plaçables n'est pas égal à 20")

        if not hasattr(joueurs, '__iter__'):
            raise QuoridorError("Argument joueurs n'est pas itérable")

        if len(joueurs) > 2:
            raise QuoridorError("Plus de deux joueurs")


    def afficher(self):
        'g'

