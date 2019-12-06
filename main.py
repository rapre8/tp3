import argparse
import random
from itertools import product
import networkx as nx
from api import lister_parties, débuter_partie, jouer_coup
from quoridor import QuoridorError, Quoridor



#on pose la vairable gamestate, avec laquelle ma fonction a été programée


#première fonction, sert à récupérer les commanees tapées dans le terminal
def analyser_commande():
    parser = argparse.ArgumentParser(description="Jeu Quoridor")

    parser.add_argument('idul', type=str, help='IDUL du joueur.')

    parser.add_argument('-a', 'automatique', action = 'store_true',
    help='pour jouer en mode automatique contre le serveur avec le nom spécifié')

    parser.add_argument('-x', 'graphique', action = 'store_true',
    help='pour jouer en mode manuel contre le serveur avec le nom spécifié, mais avec un affichage dans une fenêtre graphique.')

    parser.add_argument('-ax', 'automatique_graphique', action = 'store_true',
    help='pour jouer en mode automatique contre le serveur avec le nom spécifié, mais avec un affichage dans une fenêtre graphique.')
    args = parser.parse_args()
    analyser_commande.idul = args.idul
    
    return args

#sert à activer la fonction analyser commande
if __name__ =='__main__':
    analyser_commande()


