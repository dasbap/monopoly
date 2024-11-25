from joueur import Joueur, Banque, banque
from abc import ABC, abstractmethod
from typing import List
import mysql.connector

class Zone(ABC):
    def __init__(self, couleur: str = "", prix_maison: int = 0):
        self.id_bdd: int = None
        self.couleur = couleur
        self.prix_maison: int = prix_maison
        self.proprietes: list[Propriete] = []  

    def ajouter_propriete(self, propriete: 'Propriete') -> None:
        """Ajoute une propriété à la zone."""
        self.proprietes.append(propriete)

    @classmethod
    def importer_un(cls, id):
        """Importe une zone par son ID."""
        mydb = Zone.connexion_bdd()
        mycursor = mydb.cursor(dictionary=True)
        zone = None
        try:
            mycursor.execute("""
                SELECT id, nom, couleur, prix_maison FROM Zone WHERE id = %s;
            """, (id,))
            result = mycursor.fetchone()
            if result:
                zone = Zone(result["nom"], result["couleur"], result["prix_maison"])
                zone.id_bdd = result["id"]
        except Exception as e:
            print(f"Erreur lors de l'importation de la zone: {e}")
        return zone

    @classmethod
    def connexion_bdd(cls):
        """Établit la connexion à la base de données."""
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="monopoly"
        )
        return mydb


class Propriete(ABC):
    def __init__(self, prix_achats: int, nom: str, loyer: List[int], zone: Zone):
        self.__prix_achats: int = prix_achats
        self.__nom: str = nom
        self.__valeur_hypoteque: int = prix_achats / 2
        self.__est_hypoteque: bool = False
        self.zone: Zone = zone
        self.__proprietaire: Joueur = banque
        self.loyer: List[int] = loyer
        self.zone.ajouter_propriete(self)

    def __str__(self) -> str:
        return f"{self.nom} - Prix d'achat: {self.prix_achats} € - Propriétaire: {self.proprietaire.nom if self.proprietaire else 'aucun'}"

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def valeur_hypoteque(self) -> int:
        return self.__valeur_hypoteque

    @property
    def est_hypoteque(self) -> bool:
        return self.__est_hypoteque

    @property
    def prix_achats(self) -> int:
        return self.__prix_achats

    @prix_achats.setter
    def prix_achats(self, value: int) -> None:
        self.__prix_achats = value

    @property
    def zone(self) -> Zone:
        return self.__zone

    @zone.setter
    def zone(self, value: Zone) -> None:
        self.__zone = value
    
    @property
    def proprietaire(self) -> Joueur:
        return self.__proprietaire

    @proprietaire.setter
    def proprietaire(self, value: Joueur) -> None:
        self.__proprietaire = value

    def achete(self, joueur: Joueur) -> None:
        """Permet à un joueur d'acheter la propriété si elle n'a pas déjà de propriétaire."""
        if not self.proprietaire:
            self.proprietaire = joueur
            joueur.argent -= self.prix_achats
            joueur.ajouter_propriete(self)
            print(f"{joueur.nom} a acheté {self.nom} pour {self.prix_achats} €. ")
        else:
            print(f"{self.nom} est déjà possédée par {self.proprietaire.nom}.")

    def vendre(self, joueur: Joueur) -> None:
        """Permet à un joueur de vendre la propriété s'il en est le propriétaire."""
        if self.proprietaire == joueur:
            joueur.argent += self.prix_achats
            joueur.retirer_propriete(self)
            self.proprietaire = None
            print(f"{joueur.nom} a vendu {self.nom} pour {self.prix_achats} €. ")
        else:
            print(f"{joueur.nom} ne possède pas {self.nom}.")

    def hypoteque(self) -> None:
        """Met la propriété en hypothèque."""
        if not self.est_hypoteque:
            self.__est_hypoteque = True
            if self.proprietaire:
                self.proprietaire.argent += self.valeur_hypoteque
            print(f"{self.nom} est maintenant hypothéquée pour {self.valeur_hypoteque} €. ")
        else:
            print(f"{self.nom} est déjà hypothéquée.")

    def liberer_hypoteque(self) -> None:
        """Libère la propriété de l'hypothèque en payant des frais."""
        if self.est_hypoteque:
            frais: int = int(self.valeur_hypoteque * 0.1)
            cout_total: int = self.valeur_hypoteque + frais
            if self.proprietaire and self.proprietaire.argent >= cout_total:
                self.proprietaire.argent -= cout_total
                self.__est_hypoteque = False
                print(f"{self.nom} est libérée de l'hypothèque pour {cout_total} €. ")
            else:
                print(f"{self.proprietaire.nom} n'a pas assez d'argent pour libérer {self.nom}.")
        else:
            print(f"{self.nom} n'est pas hypothéquée.")

    @abstractmethod
    def calculer_loyer(self) -> int:
        pass

    def est_proprietaire(self, joueur: Joueur) -> bool:
        """Vérifie si un joueur est le propriétaire de la propriété."""
        return self.proprietaire == joueur

    @classmethod
    def connexion_bdd(cls):
        """Établit la connexion à la base de données."""
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="monopoly"
        )
        return mydb

    def sauvegarde_bdd(self):
        """Sauvegarde la propriété dans la base de données, avec une référence à la zone."""
        mydb = Propriete.connexion_bdd()
        monCurseur = mydb.cursor()
        if hasattr(self, 'id_bdd') and self.id_bdd:
            monCurseur.execute("""
                UPDATE Propriete SET nom = %s, prix_achats = %s, zone_id = %s WHERE id = %s
            """, (self.nom, self.prix_achats, self.zone.id_bdd, self.id_bdd))
            mydb.commit()
            print(f"La propriété {self.nom} a été mise à jour dans la base de données.")
        else:
            monCurseur.execute("""
                INSERT INTO Propriete (nom, prix_achats, zone_id) VALUES (%s, %s, %s)
            """, (self.nom, self.prix_achats, self.zone.id_bdd))
            mydb.commit()
            self.id_bdd = monCurseur.lastrowid
            print(f"La propriété {self.nom} a été sauvegardée dans la base de données avec l'ID {self.id_bdd}.")

    @classmethod
    def importer_un(cls, id):
        """Importe une propriété par son ID."""
        mydb = Propriete.connexion_bdd()
        mycursor = mydb.cursor(dictionary=True)
        propriete = None
        try:
            mycursor.execute("""
                SELECT id, nom, prix_achats, zone_id FROM Propriete WHERE id = %s;
            """, (id,))
            result = mycursor.fetchone()
            if result:
                zone = Zone.importer_un(result["zone_id"])  
                propriete = Propriete(result["prix_achats"], result["nom"], [], zone)
                propriete.id_bdd = result["id"]
        except Exception as e:
            print(f"Erreur lors de l'importation de la propriété: {e}")
        return propriete

if __name__ == '__main__':
    try:
        banque: Banque = Banque() 
        zone: Zone = Zone("bleu foncé", 200)
        p: Propriete = Propriete(400, "rue de la paix", [50, 100, 150], zone)
        print(p)

        try:
            print(p.__nom) 
        except AttributeError:
            print("__nom n'est pas accessible directement")

        print(p.nom)  
    except Exception as e:
        print(f"Erreur lors de l'instanciation de la classe Propriete: {e}")
