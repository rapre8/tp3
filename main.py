
import argparse
import random
from itertools import product
import networkx as nx
from api import débuter_partie, jouer_coup
from quoridor import QuoridorError, Quoridor



#on pose la vairable gamestate, avec laquelle ma fonction a été programée


#première fonction, sert à récupérer les commanees tapées dans le terminal
def analyser_commande():
    parser = argparse.ArgumentParser(description="Jeu Quoridor - phase 3")

    parser.add_argument('idul', type=str, help='IDUL du joueur.')

    parser.add_argument('-a', '--automatique', action = 'store_true',
    help='Activer le mode automatique.')

    parser.add_argument('-x', '--graphique', action = 'store_true',
    help='Activer le mode graphique.')

    args = parser.parse_args()
    analyser_commande.idul = args.idul
    
    if args.automatique:
        print('auto')
    
    if args.graphique:
        print('graphe')

    return args

#sert à activer la fonction analyser commande
if __name__ =='__main__':
    analyser_commande()


