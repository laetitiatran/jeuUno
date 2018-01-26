from Cartes import Cartes
from random import shuffle

class JeuCartes:

    def __init__(self, empty=False):
        self.__Cartes = []

        if not empty:
            for val in range(0,14):
                for coul in range(4):
                    self.__Cartes.append(Cartes(val, coul))

    def mix(self):
       shuffle(self.__Cartes)

    def tirer(self):
        try:
           return self.__Cartes.pop(0)
        except IndexError:
            print("Il n'y a plus cartes")
            return None

    def __getCartes(self):
        return self.__Cartes

    def __setCartes(self, Cartes):
        if len(self.__Cartes) > 52:
            raise Exception("Jeu complet")
        self.__Cartes.append(Cartes)

    Cartes = property(__getCartes, __setCartes)
