from propriete import Propriete

class Gare(Propriete):
    Loyer = [None, 0,0,0,0]
    def __init__(self, prix_achats : int, nom : str, valeur_hypoteque : int, places_dispo : int):
        super().__init__(prix_achats, nom, valeur_hypoteque)