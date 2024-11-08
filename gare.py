from propriete import Propriete
from zone import Zone, zone_gare

class Gare(Propriete):
    Loyer = [0,25,50,100,200]
    prix_achats = 200
    def __init__(self, nom : str):
        super().__init__(Gare.prix_achats, nom, Gare.Loyer, zone_gare)
    
    def __repr__(self):
        return self.__str__()

    def calculer_loyer(self) -> int:
        if not isinstance(self.zone, Zone): return -1
        return self.loyer[self.zone.nb_proprietes_possedees(self.proprietaire)]

gare1 = Gare("Montparnasse")
gare2 = Gare("Lyon")
gare3 = Gare("Saint-Lazare")
gare4 = Gare("du Nord")

if __name__ == "__main__":
    for gare in [gare1, gare2, gare3,gare4 ]:
        print(gare.calculer_loyer())
        print(gare.proprietaire)

