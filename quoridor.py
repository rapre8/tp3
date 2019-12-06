'''Programme qui permet d'utiliser l'intelligence artificielle'''
import random
from itertools import product
import networkx as nx


class QuoridorError(Exception):
    '''Classe QuoridorError'''

# FONCTION FOURNIE
def construire_graphe(joueurs, murs_horizontaux, murs_verticaux):
    """
    Crée le graphe des déplacements admissibles pour les joueurs.

    :param joueurs: une liste des positions (x,y) des joueurs.
    :param murs_horizontaux: une liste des positions (x,y) des murs horizontaux.
    :param murs_verticaux: une liste des positions (x,y) des murs verticaux.
    :returns: le graphe bidirectionnel (en networkX) des déplacements admissibles.
    """
    graphe = nx.DiGraph()

    # pour chaque colonne du damier
    for x in range(1, 10):
        # pour chaque ligne du damier
        for y in range(1, 10):
            # ajouter les arcs de tous les déplacements possibles pour cette tuile
            if x > 1:
                graphe.add_edge((x, y), (x-1, y))
            if x < 9:
                graphe.add_edge((x, y), (x+1, y))
            if y > 1:
                graphe.add_edge((x, y), (x, y-1))
            if y < 9:
                graphe.add_edge((x, y), (x, y+1))

    # retirer tous les arcs qui croisent les murs horizontaux
    for x, y in murs_horizontaux:
        graphe.remove_edge((x, y-1), (x, y))
        graphe.remove_edge((x, y), (x, y-1))
        graphe.remove_edge((x+1, y-1), (x+1, y))
        graphe.remove_edge((x+1, y), (x+1, y-1))

    # retirer tous les arcs qui croisent les murs verticaux
    for x, y in murs_verticaux:
        graphe.remove_edge((x-1, y), (x, y))
        graphe.remove_edge((x, y), (x-1, y))
        graphe.remove_edge((x-1, y+1), (x, y+1))
        graphe.remove_edge((x, y+1), (x-1, y+1))

    # retirer tous les arcs qui pointent vers les positions des joueurs
    # et ajouter les sauts en ligne droite ou en diagonale, selon le cas
    for joueur in map(tuple, joueurs):

        for prédécesseur in list(graphe.predecessors(joueur)):
            graphe.remove_edge(prédécesseur, joueur)

            # si admissible, ajouter un lien sauteur
            successeur = (2*joueur[0]-prédécesseur[0], 2*joueur[1]-prédécesseur[1])

            if successeur in graphe.successors(joueur) and successeur not in joueurs:
                # ajouter un saut en ligne droite
                graphe.add_edge(prédécesseur, successeur)

            else:
                # ajouter les liens en diagonal
                for successeur in list(graphe.successors(joueur)):
                    if prédécesseur != successeur and successeur not in joueurs:
                        graphe.add_edge(prédécesseur, successeur)

    # ajouter les noeuds objectifs des deux joueurs
    for x in range(1, 10):
        graphe.add_edge((x, 9), 'B1')
        graphe.add_edge((x, 1), 'B2')

    return graphe
# FIN DE LA FONCTION FOURNIE

class Quoridor:
    '''Classe Quoridor'''
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

    def __str__(self):
        nom1 = f'1={self.gamestate["joueurs"][0]["nom"]}, '
        nom2 = f'2={self.gamestate["joueurs"][1]["nom"]}'
        haut = f'Légende:' + nom1 + nom2 + '\n'
        haut += '   -----------------------------------\n'
        bas = '--|-----------------------------------\n'
        bas += '  | 1   2   3   4   5   6   7   8   9'
        liste_vide = []
        for i in range(18, 1, -1):
            style_damier_1 = list(f"{i//2} | .   .   .   .   .   .   .   .   . |")
            style_damier_2 = list("  |                                   |")
            if i%2 == 0:
                liste_vide.append(style_damier_1)
            else:
                liste_vide.append(style_damier_2)
        for i in range(2):
            x = 18-2*self.gamestate["joueurs"][i]["pos"][1]
            y = 4*self.gamestate["joueurs"][i]["pos"][0]
            liste_vide[x][y] = f'{i+1}'
        for i in range(len(self.gamestate["murs"]["horizontaux"])):
            for j in range(7):
                x = 19-2*self.gamestate["murs"]["horizontaux"][i][1]
                y = 4*self.gamestate["murs"]["horizontaux"][i][0]+j-1
                liste_vide[x][y] = '-'
        for i in range(len(self.gamestate["murs"]["verticaux"])):
            for j in range(3):
                x = 18-2*self.gamestate["murs"]["verticaux"][i][1]-j
                y = 4*self.gamestate["murs"]["verticaux"][i][0]-2
                liste_vide[x][y] = '|'
        damier = []
        for ligne in liste_vide:
            damier += ligne + ['\n']
        milieu = ''.join(damier)

        return haut + milieu + bas

    def déplacer_jeton(self, joueur, position):
        '''Permet de déplacer le jeton'''
        if joueur != 1:
            if joueur != 2:
                raise QuoridorError('le numéro du joueur doit être 1 ou 2')

        if position[0] > 9 or position[0] < 1 or position[1] > 9 or position[1] < 1:
            raise QuoridorError('la position est invalide (en dehors du damier)')

        nouvelle_position = list(position)
        self.gamestate['joueurs'][joueur - 1]['pos'] = nouvelle_position

    def état_partie(self):
        '''Retourne l'état de la partie'''
        return self.gamestate

    def jouer_coup(self, joueur):
        '''Permet de jouer automatiquement le coup'''

        graphe = construire_graphe(
            [joueur['pos'] for joueur in self.gamestate['joueurs']],
            self.gamestate['murs']['horizontaux'],
            self.gamestate['murs']['verticaux'])


        position_a_aller_j1 = nx.shortest_path(
            graphe,
            tuple(self.gamestate['joueurs'][0]['pos']), 'B1')

        position_a_aller_j2 = nx.shortest_path(
            graphe,
            tuple(self.gamestate['joueurs'][1]['pos']), 'B2')

        if joueur == 1:
            if len(position_a_aller_j1) <= len(position_a_aller_j2):
                self.déplacer_jeton(joueur, position_a_aller_j1[1])

            else:
                if self.gamestate['joueurs'][0]['murs'] == 0:
                    self.déplacer_jeton(joueur, position_a_aller_j1[1])
                try:
                    x = random.randint(1, 9)
                    y = random.randint(1, 9)
                    orientation = random.choice(['horizontal', 'vertical'])
                    self.placer_mur(1, (x, y), orientation)
                    self.gamestate['joueurs'][0]['murs'] -= 1
                except QuoridorError:
                    self.jouer_coup(1)

        if joueur == 2:
            if len(position_a_aller_j1) >= len(position_a_aller_j2):
                self.déplacer_jeton(joueur, position_a_aller_j2[1])


            else:
                if self.gamestate['joueurs'][1]['murs'] == 0:
                    self.déplacer_jeton(joueur, position_a_aller_j2[1])
                try:
                    x = random.randint(1, 9)
                    y = random.randint(1, 9)
                    orientation = random.choice(['horizontal', 'vertical'])
                    self.placer_mur(1, (x, y), orientation)
                    self.gamestate['joueurs'][1]['murs'] -= 1
                except QuoridorError:
                    self.jouer_coup(2)

    def partie_terminée(self):
        '''Permet de savoir si la partie est terminée'''
        if self.gamestate['joueurs'][0]['pos'][1] == 9:
            return self.gamestate['joueurs'][0]["nom"]
        if self.gamestate['joueurs'][1]['pos'][1] == 1:
            return self.gamestate['joueurs'][1]["nom"]
        return False

    def placer_mur(self, joueur: int, position: tuple, orientation: str):
        '''Permet de placer un mur sur le damier'''
        if joueur != 1:
            if joueur != 2:
                raise QuoridorError('le numéro du joueur doit être 1 ou 2')

        if self.gamestate['joueurs'][joueur-1]['murs'] == 0:
            raise QuoridorError('le joueur a déjà placé tous ses murs')

        murs_horiz = self.gamestate['murs']['horizontaux']
        murs_verti = self.gamestate['murs']['verticaux']
        if position in murs_horiz or position in murs_verti:
            raise QuoridorError('un mur occupe déjà cette position')

        self.gamestate['joueurs'][joueur-1]['murs'] = self.gamestate['joueurs'][joueur-1]['murs']-1
        if orientation == 'horizontal':
            self.gamestate['murs']['horizontaux'].append(position)
        if orientation == 'vertical':
            self.gamestate['murs']['verticaux'].append(position)

        for i in self.gamestate['murs']['verticaux']:
            if i[0] < 2 or i[1] > 8:
                self.gamestate['murs']['verticaux'].pop()
                raise QuoridorError("Position mur vertical invalide")
            if i not in list(product(range(1, 10), repeat=2)):
                self.gamestate['murs']['verticaux'].pop()
                raise QuoridorError("Position mur vertical invalide")

        for i in self.gamestate['murs']['horizontaux']:
            if i[0] > 8 or i[1] < 2:
                self.gamestate['murs']['horizontaux'].pop()
                raise QuoridorError("Position mur horizontal invalide")
            if i not in list(product(range(1, 10), repeat=2)):
                self.gamestate['murs']['horizontaux'].pop()
                raise QuoridorError("Position mur horizontal invalide")
