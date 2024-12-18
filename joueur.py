from abc import ABC, abstractmethod
class Zone:
    def __init__(self, couleur: str = "", prix_maison: int = 0):
        self.id_bdd: int = None
        self.couleur = couleur
        self.prix_maison: int = prix_maison
        self.proprietes = []  
    
    def __str__(self):
        """Affiche les informations de la zone."""
        pass
    
    def __repr__(self):
        return self.__str__()

    def ajouter_propriete(self, propriete: 'Propriete'):
        """Ajoute une propriété à la zone et définit sa zone."""
        pass
    
    def nb_proprietes_possedees(self, joueur: 'Joueur') -> int:
        """Renvoie le nombre de propriétés possédées par un joueur dans cette zone."""
        pass
    
    def sauvegarde_bdd(self):
        pass
    def est_monopole(self, joueur) -> bool:
        """Vérifie si le joueur possède toutes les propriétés de la zone."""
        pass

class Propriete(ABC):
    def __init__(self, prix_acquisition: int, nom: str, loyer: list[int], zone: Zone):
        self.prix_acquisition: int = prix_acquisition
        self.nom: str = nom
        self.loyer: list[int] = loyer
        self.zone: Zone = zone
        self.proprietaire: Joueur = banque

class Terrain(Propriete):
    def __init__(self, nom, zone: Zone, prix_acquisition: int, loyer: list[int]):
        super().__init__(prix_acquisition, nom, loyer, zone)
        self.nb_maisons = 0
        self.prix_maisons : int

    def calculer_loyer(self) -> int:
        """Calcule le loyer en fonction du nombre de maisons et de la zone."""
        pass

    def ajouter_maison(self, joueur: 'Joueur'):
        """Ajoute une maison sur le terrain si le joueur possède toutes les propriétés nécessaires."""
        pass

    def ajouter_hotel(self, joueur: 'Joueur'):
        """Ajoute un hôtel si les conditions sont remplies."""
        pass

################################################################################################

class Joueur():
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
    
    def ajouter_propriete(self, propriete : Propriete):
        self.proprietes.append(propriete)
        propriete.proprietaire = self

class Banque(Joueur):
    def __init__(self):
        super().__init__("banque", 20580)
    

class Vrais_Joueur(Joueur):
    nb_joueur = 1
    def __init__(self) -> None:
        nom = input(f"Quel est le nom du joueur {Vrais_Joueur.nb_joueur} :")
        super().__init__(nom, 1500)
        self.position = 0
    
    def avance(self):
        pass

banque = Banque()
