from propriete import Propriete
from zone import Zone

class Gare(Propriete):
    Loyer = [0,25,50,100,200]
    def __init__(self, nom : str, prix_achats : int = 200):
        super().__init__(prix_achats, nom, Gare.Loyer)
    
    def calculer_loyer(self) -> int:
        if not isinstance(self.zone, Zone): return -1
        return self.loyer[self.zone.nb_proprietes_possedees(self.proprietaire)]