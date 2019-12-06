import requests


# définition de la fonction lister_parties, qui, en premier lieu, 
# soit réussit à contacter le serveur (rep.status_code == 200),
# soit non, dans lequel cas la fonction affiche un message d'erreur.
# Une fois le serveur contacté, le dictionnaire est décodé, et s'il contient l'argument 'message',
# il embarque dans le processus d'erreur, au cours duquel il raise une erreur de type RuntimeError
# et retourne le message d'erreur du dictionnaire.

def lister_parties(idul):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'

    rep = requests.get(url_base+'lister/', params={'idul': f'{idul}'})
    if rep.status_code == 200:
        rep = rep.json()
        try:
            if "message" in rep:
                raise RuntimeError
            else:
                return rep
        except RuntimeError:
            return (rep['message'])
        

    else:
        print(f"Le GET sur {url_base+'lister'} a produit le code d'erreur {rep.status_code}.")

# Même principe que pour la fonction précédente,
# mais retourne l'id de partie débutée et l'état du damier.
        
def débuter_partie(idul):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'

    rep = requests.post(url_base+'débuter/', data={'idul': f'{idul}'})
    
    rep = rep.json()
    try:
        if "message" in rep:
            raise RuntimeError
        else:
            return (rep['id'],rep['état'])
    except RuntimeError:
        return (rep['message'])
        
# explications

def jouer_coup(id_partie, type_coup, position):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'

    rep = requests.post(url_base+'jouer/', data={'id': f'{id_partie}', 'type': f'{type_coup}', 'pos': f'{position}'})
    
    rep = rep.json()
    try:
        if "message" in rep:
            raise RuntimeError
        elif "gagnant" in rep:
            raise StopIteration
        else:
            return (rep['état'])
    except (RuntimeError, StopIteration):
        if "message" in rep:
            return (rep['message'])
        elif "gagnant" in rep:
            return (rep['gagnant'])

# ok
