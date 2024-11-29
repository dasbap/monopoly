from abc import ABC, abstractmethod

class Joueur(ABC):
    def __init__(self,nom,argent) -> None:
        self.nom = nom
        self.argent = argent
        self.proprietes = []
    
    def __str__(self) -> str:
        return f"Joueur : {self.nom}, Argent : {self.argent}"
    
    def donner_argent(self, Joueur: 'Joueur', argent) -> None:
        if self.argent >= argent:
            Joueur.argent += argent
        else:
            print(f"{self.nom} ne possède pas assez d'argent.")
    
    
    @abstractmethod
    def ajouter_propriete(self, propriete):
        pass

class Banque(Joueur):
    def __init__(self):
        super().__init__("banque", 20580)
    
    def ajouter_propriete(self, propriete):
        pass

class Vrais_Joueur(Joueur):
    nb_joueur = 1
    def __init__(self) -> None:
        nom = input(f"Quel est le nom du joueur {Vrais_Joueur.nb_joueur} :")
        super().__init__(nom, 1500)
        

banque = Banque()