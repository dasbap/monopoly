from propriete import Propriete
from joueur import Joueur
import mysql.connector

class Zone:
    def __init__(self, couleur: str = "", prix_maison: int = 0):
        self.id_bdd: int = None
        self.couleur = couleur
        self.prix_maison: int = prix_maison
        self.proprietes: list[Propriete] = []  
    
    def __str__(self):
        """Affiche les informations de la zone."""
        proprietes_nom = ', '.join([propriete.nom for propriete in self.proprietes])
        return f"Zone: {self.couleur}, Propriétés: {proprietes_nom}, Prix Maison: {self.prix_maison} €"
    
    def __repr__(self):
        return self.__str__()

    def ajouter_propriete(self, propriete: Propriete):
        """Ajoute une propriété à la zone et définit sa zone."""
        if propriete.zone is self:
            self.proprietes.append(propriete)
            propriete.zone = self
            print(f"{propriete.nom} a été ajouté à la zone {self.couleur}.")
        else:
            print(f"{propriete.nom} appartient déjà à la zone {propriete.zone.nom}.")
    
    def nb_proprietes_possedees(self, joueur: Joueur) -> int:
        """Renvoie le nombre de propriétés possédées par un joueur dans cette zone."""
        return sum(1 for propriete in self.proprietes if propriete.proprietaire == joueur)
    
    def est_monopole(self, joueur) -> bool:
        """Vérifie si le joueur possède toutes les propriétés de la zone."""
        return all(propriete.proprietaire == joueur for propriete in self.proprietes)
    
    @classmethod
    def connexion_bdd(cls):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="monopoly"
            )
            return mydb
        except mysql.connector.Error as e:
            print(f"Erreur de connexion à la base de données: {e}")
            return None

    
    def sauvegarde_bdd(self):
        mydb = Zone.connexion_bdd()
        monCurseur = mydb.cursor()
        monCurseur.execute("SELECT id FROM Zone WHERE couleur = %s", (self.couleur,))
        result = monCurseur.fetchone()
        if result:
            self.id_bdd = result[0]
            print(f"La zone {self.couleur} existe déjà avec l'ID {self.id_bdd}.")
        else:
            monCurseur.execute(
                "INSERT INTO Zone (couleur, prix_maison) VALUES (%s, %s)",
                (self.couleur, self.prix_maison)
            )
            mydb.commit()
            self.id_bdd = monCurseur.lastrowid 
            print(f"Zone sauvegardée dans la base de données avec l'ID {self.id_bdd}.")
    
    @classmethod
    def importer_un(cls, id):
        mydb = Zone.connexion_bdd()
        mycursor = mydb.cursor(dictionary=True)
        z = None
        try:
            mycursor.execute("""
                            SELECT id, couleur, prix_maison
                            FROM Zone
                            WHERE id = %s;""", (id,))
            result = mycursor.fetchone()
            if result:
                z = Zone(result["couleur"], result["prix_maison"])
                z.id_bdd = result["id"] 
        except Exception as e:
            print(f"Erreur lors de l'importation de la zone: {e}")
        return z 
    
    @classmethod
    def importer_tous(cls):
        mydb = Zone.connexion_bdd()
        mycursor = mydb.cursor(dictionary=True)
        zones = []
        try:
            mycursor.execute("""
                            SELECT id, couleur, prix_maison
                            FROM Zone;""")
            results = mycursor.fetchall()
            for result in results:
                z = Zone(result["couleur"], result["prix_maison"])
                z.id_bdd = result["id"]  
                zones.append(z)  
        except Exception as e:
            print(f"Erreur lors de l'importation des zones: {e}")
        return zones  
    
    @classmethod
    def creation_table(cls):
        mydb = Zone.connexion_bdd()
        monCurseur = mydb.cursor()
        monCurseur.execute("""CREATE TABLE IF NOT EXISTS Zone (
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
        monCurseur.execute("DROP TABLE IF EXISTS Zone")


zone_gare = Zone("noir")
zone_companie = Zone("blanc")

zone_residanciel = {
    "bleu foncé": Zone("bleu foncé", 200),
    "bleu clair": Zone("bleu clair", 50),
    "rouge": Zone("rouge", 150),
    "jaune": Zone("jaune",150),
    "vert": Zone("vert", 200),
    "orange": Zone("orange", 100),
    "maron": Zone("maron",50),
    "violet": Zone("violet", 100),
}

Zone.creation_table()

for zone in zone_residanciel:
    zone_residanciel[zone].sauvegarde_bdd()

zone_residanciel["bleu foncé"].sauvegarde_bdd()
zone_residanciel["violet"].sauvegarde_bdd() 

zone_gare.sauvegarde_bdd()
zone_companie.sauvegarde_bdd()

zone_alea = Zone.importer_un(8)

print(f"Zone importée : {zone_alea}" if zone_alea else "Aucune zone importée.")

print(f"Toutes les Zones importable : {Zone.importer_tous()}")