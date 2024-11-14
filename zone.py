from propriete import Propriete
from joueur import Joueur
import mysql.connector

class Zone:
    def __init__(self, couleur : str = "", prix_maison: int = 0):
        self.couleur = couleur
        self.prix_maison : int = prix_maison
        self.proprietes: list[Propriete] = []  

    def ajouter_propriete(self, propriete: Propriete):
        """Ajoute une propriété à la zone et définit sa zone."""
        if propriete.zone is self:
            self.proprietes.append(propriete)
            propriete.zone = self
            print(f"{propriete.nom} a été ajouté à la zone {self.__class__.__name__}.")
        else:
            print(f"{propriete.nom} appartient déjà à la zone {propriete.zone.nom}.")
    
    def nb_proprietes_possedees(self, joueur : Joueur) -> int:
        """Renvoie le nombre de propriétés possédées par un joueur dans cette zone."""
        return sum(1 for propriete in self.proprietes if propriete.proprietaire == joueur)
    
    def est_monopole(self, joueur) -> bool:
        """Vérifie si le joueur possède toutes les propriétés de la zone."""
        return all(propriete.proprietaire == joueur for propriete in self.proprietes)
    
    def __str__(self):
        """Affiche les informations de la zone."""
        proprietes_nom = ', '.join([propriete.nom for propriete in self.proprietes])
        return f"Zone: {self.__class__.__name__}, Propriétés: {proprietes_nom}, Prix Maison: {self.prix_maison} €"
    
    @classmethod
    def connexion_bdd(cls):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "monopoly"
        )
        return mydb
    
    @classmethod
    def creation_table(cls):
        mydb = Zone.connexion_bdd()
        monCurseur = mydb.cursor()
        monCurseur.execute("""CREATE TABLE IF NOT EXISTS Quartiers (
                        id INT NOT NULL UNIQUE AUTO_INCREMENT,
                        couleur VARCHAR(255),
                        prix_maison INT NOT NULL,
                        PRIMARY KEY(id)
                        )
                        """)
    
    @classmethod
    def suppression_table(cls):
        mydb = Zone.connexion_bdd()
        monCurseur = mydb.cursor()
        monCurseur.execute("DROP TABLE IF EXISTS Quartiers")


zone_gare = Zone("noir")
zone_companie = Zone("blanc")

zone_residanciel = {
    "bleu foncé" : Zone("bleu foncé"),
    "bleu clair" : Zone("bleu clair"),
    "rouge" : Zone("rouge"),
    "jaune" : Zone("jaune"),
    "vert" : Zone("vert"),
    "orange" : Zone("orange"),
    "rose" : Zone("rose"),
    "maron" : Zone("maron")
}

Zone.creation_table()