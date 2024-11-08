from propriete import Propriete
from zone import Zone, zone_gare

class Gare(Propriete):
    Loyer = [0,25,50,100,200]
    prix_achats = 200
    def __init__(self, nom : str):
        super().__init__(Gare.prix_achats, nom, Gare.Loyer, zone_gare)
    def __str__(self):
        return f"Gare: {self.nom}"
    def __repr__(self):
        return self.__str__()

    
    def calculer_loyer(self) -> int:
        if not isinstance(self.zone, Zone): return -1
        return self.loyer[self.zone.nb_proprietes_possedees(self.proprietaire)]

gare1 = Gare("Cenon")

print(gare1.calculer_loyer())
print(gare1.proprietaire)
print(gare1.zone.proprietes)