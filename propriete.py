from joueur import Joueur, banque
from abc import ABC, abstractmethod

class Zone(ABC):
    def __init__(self, nom: str, couleur : str = "", prix_maison: int = 0):
        self.nom = nom
        self.couleur = couleur
        self.prix_maison : int = prix_maison
        self.proprietes: list[Propriete] = [] 

class Propriete(ABC):
    def __init__(self, prix_achats: int, nom: str, loyer : list[int], zone : Zone):
        self.__prix_achats = prix_achats
        self.__nom = nom
        self.__valeur_hypoteque = prix_achats / 2
        self.__est_hypoteque = False
        self.zone = zone
        self.__proprietaire : Joueur = banque
        self.loyer = loyer

    def __str__(self) -> str:
        return f"{self.nom} - Prix d'achat: {self.prix_achats} € - Propriétaire: {self.proprietaire.nom if self.proprietaire else 'aucun'}"

    @property
    def nom(self):
        return self.__nom

    @property
    def valeur_hypoteque(self):
        return self.__valeur_hypoteque

    @property
    def est_hypoteque(self):
        return self.__est_hypoteque

    @property
    def prix_achats(self):
        return self.__prix_achats

    @prix_achats.setter
    def prix_achats(self, value : int) -> None:
        self.__prix_achats = value

    @property
    def zone(self) -> Zone:
        return self.__zone

    @zone.setter
    def zone(self, value) -> None:
        self.__zone = value
    
    @zone.getter
    def zone(self) -> Zone:
        return self.__zone
    
    @property
    def proprietaire(self):
        return self.__proprietaire

    @proprietaire.setter
    def proprietaire(self, value : Joueur) -> None:
        self.__proprietaire = value

    def achete(self, joueur):
        """Permet à un joueur d'acheter la propriété si elle n'a pas déjà de propriétaire."""
        if not self.proprietaire:
            self.proprietaire = joueur
            joueur.argent -= self.prix_achats
            joueur.ajouter_propriete(self)
            print(f"{joueur.nom} a acheté {self.nom} pour {self.prix_achats} €. ")
        else:
            print(f"{self.nom} est déjà possédée par {self.proprietaire.nom}.")

    def vendre(self, joueur):
        """Permet à un joueur de vendre la propriété s'il en est le propriétaire."""
        if self.proprietaire == joueur:
            joueur.argent += self.prix_achats
            joueur.retirer_propriete(self)
            self.proprietaire = None
            print(f"{joueur.nom} a vendu {self.nom} pour {self.prix_achats} €. ")
        else:
            print(f"{joueur.nom} ne possède pas {self.nom}.")

    def hypoteque(self):
        """Met la propriété en hypothèque."""
        if not self.est_hypoteque:
            self.est_hypoteque = True
            if self.proprietaire:
                self.proprietaire.argent += self.valeur_hypoteque
            print(f"{self.nom} est maintenant hypothéquée pour {self.valeur_hypoteque} €. ")
        else:
            print(f"{self.nom} est déjà hypothéquée.")

    def liberer_hypoteque(self):
        """Libère la propriété de l'hypothèque en payant des frais."""
        if self.est_hypoteque:
            frais = int(self.valeur_hypoteque * 0.1)
            cout_total = self.valeur_hypoteque + frais
            if self.proprietaire and self.proprietaire.argent >= cout_total:
                self.proprietaire.argent -= cout_total
                self.est_hypoteque = False
                print(f"{self.nom} est libérée de l'hypothèque pour {cout_total} €. ")
            else:
                print(f"{self.proprietaire.nom} n'a pas assez d'argent pour libérer {self.nom}.")
        else:
            print(f"{self.nom} n'est pas hypothéquée.")

    @abstractmethod
    def calculer_loyer(self) -> int:
        pass

    def est_proprietaire(self, joueur) -> bool:
        """Vérifie si un joueur est le propriétaire de la propriété."""
        return self.proprietaire == joueur


if __name__ == '__main__':
    try:
        p = Propriete(400, "rue de la paix")
        print(p) 
        try:
            print(p.__nom) 
        except AttributeError:
            print("__nom n'est pas accessible directement")

        print(p.nom)  
    except:
        print("Erreur lors de l'instanciation de la class Propriete")
