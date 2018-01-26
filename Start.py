from JeuCartes import JeuCartes
from Cartes import Cartes
from Joueur import Joueur

if __name__ == "__main__":
    J1 = Joueur("Toto")
    J2 = Joueur("Lulu")

    J = JeuCartes()
    J.mix()

    try:
        while True:
            J1.ajouter()
            J2.ajouter()
    except IndexError as err:
        print("tirer")
