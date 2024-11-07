from propriete import Propriete

class Quartier:
    def __init__(self, nom: str, prix_maison: int = 0):
        self.nom = nom
        self.prix_maison = prix_maison  
        self.proprietes: list[Propriete] = [] 

    def ajouter_propriete(self, propriete: Propriete):
        """Ajoute une propriété au quartier et définit son quartier."""
        if propriete not in self.proprietes:
            self.proprietes.append(propriete)
            propriete.quartier = self
            print(f"{propriete.nom} a été ajouté au quartier {self.nom}.")
        else:
            print(f"{propriete.nom} est déjà dans le quartier {self.nom}.")

    def nb_proprietes_possedees(self, joueur) -> int:
        """Renvoie le nombre de propriétés possédées par un joueur dans ce quartier."""
        return sum(1 for propriete in self.proprietes if propriete.proprietaire == joueur)

    def est_monopole(self, joueur) -> bool:
        """Vérifie si le joueur possède toutes les propriétés du quartier."""
        return all(propriete.proprietaire == joueur for propriete in self.proprietes)
