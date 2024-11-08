class Joueur():
    def __init__(self,argent) -> None:
        self.argent = argent

class Banque(Joueur):
    def __init__(self, argent):
        super().__init__(argent)



banque = Banque(100000)