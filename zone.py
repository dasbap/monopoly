from propriete import Propriete
from joueur import Joueur

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
