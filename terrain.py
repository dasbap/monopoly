from propriete import Propriete
from zone import Zone, zone_residanciel
from joueur import Joueur

class Terrain(Propriete):
    def __init__(self, nom, zone : Zone, prix_acquisition, loyer : list[int, int, int, int, int, int]):
        super().__init__(prix_acquisition,loyer, nom, zone)
        self.nb_maisons = 0
        self.prix_maisons = self.zone.prix_maison
    
    def calculer_loyer(self) -> int:
        if not isinstance(self.zone,Zone): return -1
        if self.zone.est_monopole(self.proprietaire) and self.nb_maisons == 0:
            return self.loyer[1] * 2
            

    def ajouter_maison(self, joueur : Joueur):
        if not isinstance(self.zone,Zone): return None
        if self.zone.est_monopole(joueur):
            if joueur.argent >= self.prix_maisons:
                if self.nb_maisons < 4 :
                    self.nb_maisons += 1
                    joueur.argent -= self.prix_maisons
                    print(f"Une maison a été ajoutée sur {self.nom}. Il y a maintenant {self.nb_maisons} maison(s).")
                    if self.nb_maisons == 4:
                        print("un Hotel peut êtres construit")
                else :
                    print(f"Impossible d'ajouter une maison sur {self.nom}. Vérifiez les conditions.")
            else :
                print(f"Vous n'avez pas assez d'argent pour construire une maison sur {self.nom}.")
        else :
            print(f"Vous ne possédez pas toutes les propriétés de la zone {self.zone.couleur}.")
        
    def ajouter_hotel(self, joueur : Joueur):
        if not isinstance(self.zone, Zone): return
        
        if self.zone.est_monopole(joueur):
            if joueur.argent >= self.prix_maisons:
                if self.nb_maisons == 4 :
                    self.nb_maisons += 1
                    joueur.argent -= self.prix_maisons
                    print(f"Un Hotel a été ajoutée sur {self.nom}. Il y a maintenant {4} nouvelles maisons disponible.")
                else :
                    print(f"Impossible d'ajouter une maison sur {self.nom}. Vérifiez les conditions.")
            else :
                print(f"Vous n'avez pas assez d'argent pour construire une maison sur {self.nom}.")
        else :
            print(f"Vous ne possédez pas toutes les propriétés de la zone {self.zone.couleur}.")

def init_terrain():
    t = {
        Terrain("Mediterranean", zone_residanciel["maron"], 60, [2,10,30,90,160,250]),
        Terrain("Baltic", zone_residanciel["maron"], 60, [4,20,60,180,320,450]),
        Terrain("Oriental", zone_residanciel["bleu clair"], 100, [8,40,100,300,450,600]),
        Terrain("Vermont", zone_residanciel["bleu clair"], 100, [8,40,100,300,450,600]),
    }
    return t
