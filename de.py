from random import randint

class de():
    def __init__(self, nb_faces : int):
        self.nb_faces = nb_faces
        self.nb_de = 1
    
    def lance_de_de(self) -> list[int]:
        resultat = []
        for _ in range(self.nb_de):
            resultat = [randint(1, self.nb_faces)] + resultat
        return resultat

class paire_de_de(de):
    def __init__(self, nb_faces : int):
        self.nb_faces = nb_faces
        self.nb_de = 2