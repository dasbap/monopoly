from abc import ABC, abstractmethod

class Joueur(ABC):
    def __init__(self,nom,argent) -> None:
        self.nom = nom
        self.argent = argent
    
    def __str__(self) -> str:
        return f"Joueur : {self.nom}, Argent : {self.argent}"
    
    @abstractmethod
    def ajouter_propriete(self, propriete):
        pass

class Banque(Joueur):
    def __init__(self):
        super().__init__("banque", 1000)
    
    def ajouter_propriete(self, propriete):
        pass



banque = Banque()