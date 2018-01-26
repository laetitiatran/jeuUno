class Cartes:
    couleur = ("bleu", "vert", "rouge", "jaune")
    valeur = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+2", "inversion", "passer", "stop")

    def __init__(self, coul, val):
        self.valeur = val
        self.couleur = coul

    def validation(self, val, coul):
        if val > 0 or val < 14:
            raise Exception("La valeur est comprise entre 0 et 14")
        if coul > 0 or coul < 4:
            raise Exception("La couleur est comprise entre 0 et 3")

    def __str__(self):
        return str(Cartes.valeur[self.__valeur]) + " de " + (Cartes.couleur[self.__couleur])

    def __getValeur(self):
        return self.__valeur

    def __setValeur(self, val):
        self.__valeur = val

    valeur = property(__getValeur, __setValeur)

    def __getCouleur(self):
        return self.__valeur

    def __setCouleur(self, val):
        self.__couleur = val

    couleur = property(__getCouleur, __setCouleur)
