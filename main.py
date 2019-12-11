
import argparse
import random
from itertools import product
import networkx as nx
from api import lister_parties, débuter_partie, jouer_coup
from quoridor import QuoridorError, Quoridor



#on pose la vairable gamestate, avec laquelle ma fonction a été programée


#première fonction, sert à récupérer les commanees tapées dans le terminal

def mode_manuel(idul):

    tuple_id_état = débuter_partie(analyser_commande.idul)
    if len(tuple_id_état) > 1:
        partie_actuelle = Quoridor([tuple_id_état[1]['joueurs'][0]['nom'], tuple_id_état[1]['joueurs'][1]['nom']])
        print(partie_actuelle)
        while True:
            a = input('type de coup (D, MH, MV): ')
            b = input('''position de l'action (x,y): ''')
            yolo = jouer_coup(tuple_id_état[0], a, b)
            if type(yolo) == str:
                print(yolo)
                break
            afficher_damier_ascii(yolo)
    else:
        print(tuple_id_état['message'])


def décortiquer_coup_auto(pré_coup, post_coup):
    if len(post_coup['murs']['horizontaux']) + len(post_coup['murs']['verticaux']) > len(pré_coup['murs']['horizontaux']) + len(pré_coup['murs']['verticaux']):
            if len(post_coup['murs']['horizontaux']) > len(pré_coup['murs']['horizontaux']):
                return ['MH', tuple(post_coup['murs']['horizontaux'][-1])]
            else: 
                return ['MV', tuple(post_coup['murs']['verticaux'][-1])]
    else: 
        return ['D', tuple(post_coup['joueurs'][0]['pos'])]


def mode_automatique(idul):
    tuple_id_état = débuter_partie(analyser_commande.idul)
    j1 = tuple_id_état[1]['joueurs'][0]['nom']
    j2 = tuple_id_état[1]['joueurs'][1]['nom']
    a = Quoridor([j1, j2])
    print(a)
    while True:
        if a.partie_terminée() != False:
            print("Le gagnant est " + a.partie_terminée())
            break
        print(f"C'est le tour de {j1}")
        pré_coup = a.état_partie()
        a.jouer_coup(1)
        print(a)
        post_coup = a.état_partie()
        type_coup = décortiquer_coup_auto(pré_coup, post_coup)[0]
        position_coup = décortiquer_coup_auto(pré_coup, post_coup)[1]
        état_joué = jouer_coup(tuple_id_état[0], type_coup, position_coup)
        if isinstance(état_joué, str):
            print(état_joué)

        a = Quoridor(état_joué['joueurs'], état_joué['murs'])
        print(a)
        if a.partie_terminée() != False:
            print("Le gagnant est " + a.partie_terminée())
            break
        print(f"C'est le coup de {j2} ")

        print(a)


def afficher_damier_ascii(gamestate):
        nom1 = f'1={gamestate["joueurs"][0]["nom"]}, '
        nom2 = f'2={gamestate["joueurs"][1]["nom"]}'
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
            x = 18-2*gamestate["joueurs"][i]["pos"][1]
            y = 4*gamestate["joueurs"][i]["pos"][0]
            liste_vide[x][y] = f'{i+1}'
        for i in range(len(gamestate["murs"]["horizontaux"])):
            for j in range(7):
                x = 19-2*gamestate["murs"]["horizontaux"][i][1]
                y = 4*gamestate["murs"]["horizontaux"][i][0]+j-1
                liste_vide[x][y] = '-'
        for i in range(len(gamestate["murs"]["verticaux"])):
            for j in range(3):
                x = 18-2*gamestate["murs"]["verticaux"][i][1]-j
                y = 4*gamestate["murs"]["verticaux"][i][0]-2
                liste_vide[x][y] = '|'
        damier = []
        for ligne in liste_vide:
            damier += ligne + ['\n']
        milieu = ''.join(damier)

        return haut + milieu + bas

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
        mode_automatique(args.idul)
    
    if args.graphique:
        print('graphe')

    if not args.automatique or args.graphique:
        mode_manuel(args.idul)

    return args

#sert à activer la fonction analyser commande
if __name__ =='__main__':
    analyser_commande()

