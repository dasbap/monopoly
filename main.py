from propriete import Propriete
from zone import Zone
from terrain import Terrain
from gare import Gare
import random


def initialiser_plateau():
    plateau = []
    plateau.append(Terrain("Rue de la Paix", 400, 50))
    plateau.append(Gare("Gare du Nord", 200, 50))

    return plateau


def initialiser_joueurs():
    joueurs = [
        {"nom": "Joueur 1", "argent": 1500, "position": 0},
        {"nom": "Joueur 2", "argent": 1500, "position": 0},
        ]
    return joueurs


def lancer_des():
    return random.randint(1, 6) + random.randint(1, 6)


def jouer():
    plateau = initialiser_plateau()
    joueurs = initialiser_joueurs()
    partie_en_cours = True
    tour = 0

    while partie_en_cours:
        joueur = joueurs[tour % len(joueurs)]
        print(f"\n{joueur['nom']}, c'est votre tour !")

        
        deplacement = lancer_des()
        print(f"Vous avez lancé un {deplacement}")
        joueur["position"] = (joueur["position"] + deplacement) % len(plateau)
        case_actuelle = plateau[joueur["position"]]

        
        if isinstance(case_actuelle, Terrain) or isinstance(case_actuelle, Gare):
            case_actuelle.gerer_passage(joueur)
        elif isinstance(case_actuelle, Zone):
            case_actuelle.appliquer_effet(joueur)

        if joueur["argent"] <= 0:
            partie_en_cours = False
            print(f"{joueur['nom']} a perdu ! Fin de la partie.")
        
        
        tour += 1

if __name__ == "__main__":
    jouer()