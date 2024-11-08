class Joueur():
    def __init__(self,nom,argent) -> None:
        self.nom = nom
        self.argent = argent
    
    def __str__(self) -> str:
        return f"Joueur : {self.nom}, Argent : {self.argent}"

class Banque(Joueur):
    def __init__(self):
        super().__init__("banque", 1000)



banque = Banque()