from Paquet import Paquet

class Joueur:

    def __init__(self, p):
        self.__prenom = p
        self.__victoires = 0
        self.__defaites = 0
        self.__paquet = Paquet()

    def tirer(self):
        return self.__paquet.tirer()

    def ajouter(self, Cartes):
        self.__paquet.ajouter(Cartes)

    def __add__(self, Cartes):
        self.ajouter(Cartes)

    def __setPrenom(self, prenom):
        self.__prenom = prenom

    def __getPrenom(self):
        return self.__prenom

    prenom = property(__getPrenom, __setPrenom)

    def __setVictoire(self, victoire):
        self.__victoire = victoire

    def __getVictoire(self):
        return self.__victoire

    victoire = property(__getVictoire, __setVictoire)

    def __setDefaite(self, defaite):
        self.__defaite = defaite

    def __getDefaite(self):
        return self.__defaite

    defaite = property(__getDefaite, __setDefaite)
