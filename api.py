'''Permet d'interagir avec le serveur de jeu'''
import requests


def débuter_partie(idul):
    '''Permet de débuter une partie avec le serveur de jeu'''
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'

    rep = requests.post(url_base+'débuter/', data={'idul': f'{idul}'})
    if rep.status_code == 200:
        rep = rep.json()
        try:
            if "message" in rep:
                raise RuntimeError
            return (rep['id'], rep['état'])
        except RuntimeError:
            return rep['message']

    else:
        print(f"Le GET sur {url_base+'débuter'} a produit le code d'erreur {rep.status_code}.")

# explications

def jouer_coup(id_partie, type_coup, position):
    '''Permet de jouer un coup pour une partie avec le serveur de jeu'''
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'

    rep = requests.post(url_base+'jouer/', data={'id': f'{id_partie}', 'type': f'{type_coup}', 'pos': f'{position}'})
    if rep.status_code == 200:
        rep = rep.json()
        try:
            if "message" in rep:
                raise RuntimeError
            if "gagnant" in rep:
                raise StopIteration
            else:
                return rep['état']
        except (RuntimeError, StopIteration):
            if "message" in rep:
                return rep['message']
            if "gagnant" in rep:
                return rep['gagnant']

    else:
        print(f"Le GET sur {url_base+'jouer'} a produit le code d'erreur {rep.status_code}.")
