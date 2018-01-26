from JeuCartes import JeuCartes
from Cartes import Cartes

class JeuUNO(JeuCartes):
    def initialiser(self):
        for val in range(0, 14):
            for coul in range(4)
                self.Cartes.append(Cartes(val, coul))