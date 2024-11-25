from propriete import Propriete
from zone import Zone, zone_residanciel
from joueur import Joueur
import mysql.connector

class Terrain(Propriete):
    def __init__(self, nom, zone: Zone, prix_acquisition: int, loyer: list[int]):
        super().__init__(prix_acquisition, nom, loyer, zone)
        self.nb_maisons = 0
        self.prix_maisons = self.zone.prix_maison
        self.sauvegarde_bdd()

    def calculer_loyer(self) -> int:
        """Calcule le loyer en fonction du nombre de maisons et de la zone."""
        if not isinstance(self.zone, Zone):
            return -1
        if self.zone.est_monopole(self.proprietaire) and self.nb_maisons == 0:
            return self.loyer[1] * 2
        return self.loyer[self.nb_maisons]

    def ajouter_maison(self, joueur: Joueur):
        """Ajoute une maison sur le terrain si le joueur possède toutes les propriétés nécessaires."""
        if not isinstance(self.zone, Zone): return None
        if self.zone.est_monopole(joueur):
            if joueur.argent >= self.prix_maisons:
                if self.nb_maisons < 4:
                    self.nb_maisons += 1
                    joueur.argent -= self.prix_maisons
                    print(f"Une maison a été ajoutée sur {self.nom}. Il y a maintenant {self.nb_maisons} maison(s).")
                    if self.nb_maisons == 4:
                        print("Un hôtel peut être construit.")
                else:
                    print(f"Impossible d'ajouter une maison sur {self.nom}. Vérifiez les conditions.")
            else:
                print(f"Vous n'avez pas assez d'argent pour construire une maison sur {self.nom}.")
        else:
            print(f"Vous ne possédez pas toutes les propriétés de la zone {self.zone.couleur}.")

    def ajouter_hotel(self, joueur: Joueur):
        """Ajoute un hôtel si les conditions sont remplies."""
        if not isinstance(self.zone, Zone): return
        if self.zone.est_monopole(joueur):
            if joueur.argent >= self.prix_maisons:
                if self.nb_maisons == 4:
                    self.nb_maisons += 1
                    joueur.argent -= self.prix_maisons
                    print(f"Un hôtel a été ajouté sur {self.nom}.")
                else:
                    print(f"Impossible d'ajouter un hôtel sur {self.nom}. Vérifiez les conditions.")
            else:
                print(f"Vous n'avez pas assez d'argent pour construire un hôtel sur {self.nom}.")
        else:
            print(f"Vous ne possédez pas toutes les propriétés de la zone {self.zone.couleur}.")

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
        """Sauvegarde le terrain dans la base de données si il n'existe pas déjà."""
        mydb = Terrain.connexion_bdd()
        monCurseur = mydb.cursor()

        monCurseur.execute("SELECT id FROM Terrain WHERE nom = %s", (self.nom,))
        terrain_existant = monCurseur.fetchone()

        if terrain_existant:
            print(f"Le terrain {self.nom} existe déjà dans la base de données avec l'ID {terrain_existant[0]}.")
            self.id_bdd = terrain_existant[0]
        else:
            if hasattr(self, 'id_bdd') and self.id_bdd:
                monCurseur.execute("""
                    UPDATE Terrain SET nom = %s, prix_acquisition = %s, zone_id = %s, nb_maisons = %s WHERE id = %s
                """, (self.nom, self.prix_achats, self.zone.id_bdd, self.nb_maisons, self.id_bdd))
                mydb.commit()
                print(f"Le terrain {self.nom} a été mis à jour dans la base de données.")
            else:
                monCurseur.execute("""
                    INSERT INTO Terrain (nom, prix_acquisition, zone_id, nb_maisons) VALUES (%s, %s, %s, %s)
                """, (self.nom, self.prix_achats, self.zone.id_bdd, self.nb_maisons))
                mydb.commit()
                self.id_bdd = monCurseur.lastrowid
                print(f"Le terrain {self.nom} a été sauvegardé dans la base de données avec l'ID {self.id_bdd}.")


    @classmethod
    def importer_un(cls, id):
        """Importe un terrain par son ID."""
        mydb = Terrain.connexion_bdd()
        mycursor = mydb.cursor(dictionary=True)
        terrain = None
        try:
            mycursor.execute("""
                SELECT id, nom, prix_acquisition, zone_id, nb_maisons FROM Terrain WHERE id = %s;
            """, (id,))
            result = mycursor.fetchone()
            if result:
                zone = Zone.importer_un(result["zone_id"]) 
                terrain = Terrain(result["nom"], zone, result["prix_acquisition"], [0, 0, 0, 0, 0, 0])
                terrain.id_bdd = result["id"]
        except Exception as e:
            print(f"Erreur lors de l'importation du terrain: {e}")
        return terrain

def init_terrain():
    """Initialise les terrains avec des zones prédéfinies."""
    terrains = {
        Terrain("Boulvard de belleville", zone_residanciel["maron"], 60, [2, 10, 30, 90, 160, 250]),
        Terrain("Rue lecourbe", zone_residanciel["maron"], 60, [4, 20, 60, 180, 320, 450]),
        Terrain("Rue de vaugiard", zone_residanciel["bleu clair"], 100, [6, 30, 90, 270, 400, 550]),
        Terrain("Rue de courcelles", zone_residanciel["bleu clair"], 100, [6, 30, 90, 270, 400, 550]),
        Terrain("Avenue de la republique", zone_residanciel["bleu clair"], 120, [8,40,100,300,450,600]),
        Terrain("Boulvard de la villet", zone_residanciel["violet"], 140, [10,50,150,450,625,750]),
    }
    return terrains
terrain = init_terrain()