class Propriete():
    def __init__(self, prix_achats: int, nom: str):
        self.prix_achats = prix_achats
        self.nom = nom
        self.valeur_hypoteque = prix_achats / 2
        self.est_hypoteque = False
        self.quartier = None 
        self.proprietaire = None  

    def achete(self, joueur):
        """Achète la propriété si elle est disponible."""
        if not self.proprietaire:
            self.proprietaire = joueur
            joueur.argent -= self.prix_achats
            joueur.ajouter_propriete(self)
            print(f"{joueur.nom} a acheté {self.nom} pour {self.prix_achats} €.")
        else:
            print(f"{self.nom} est déjà possédée par {self.proprietaire.nom}.")

    def vendre(self, joueur):
        """Vend la propriété si elle est possédée par le joueur."""
        if self.proprietaire == joueur:
            joueur.argent += self.prix_achats
            joueur.retirer_propriete(self)
            self.proprietaire = None
            print(f"{joueur.nom} a vendu {self.nom} pour {self.prix_achats} €.")
        else:
            print(f"{joueur.nom} ne possède pas {self.nom}.")

    def hypoteque(self):
        """Met la propriété en hypothèque, si elle n'est pas déjà hypothéquée."""
        if not self.est_hypoteque:
            self.est_hypoteque = True
            if self.proprietaire:
                self.proprietaire.argent += self.valeur_hypoteque
            print(f"{self.nom} est maintenant hypothéquée pour {self.valeur_hypoteque} €.")
        else:
            print(f"{self.nom} est déjà hypothéquée.")

    def liberer_hypoteque(self):
        """Libère la propriété de son hypothèque, avec des frais de 10% de la valeur hypothécaire."""
        if self.est_hypoteque:
            frais = int(self.valeur_hypoteque * 0.1)
            cout_total = self.valeur_hypoteque + frais
            if self.proprietaire and self.proprietaire.argent >= cout_total:
                self.proprietaire.argent -= cout_total
                self.est_hypoteque = False
                print(f"{self.nom} est libérée de l'hypothèque pour {cout_total} €.")
            else:
                print(f"{self.proprietaire.nom} n'a pas assez d'argent pour libérer {self.nom}.")
        else:
            print(f"{self.nom} n'est pas hypothéquée.")

    def calculer_loyer(self) -> int:
        """Calcule le loyer en fonction du nombre de propriétés dans le même quartier."""
        if self.est_hypoteque:
            return 0
        loyer_de_base = 50
        if self.quartier:
            loyer = loyer_de_base * (1 + self.quartier.nb_proprietes_possedees(self.proprietaire))
            print(f"Loyer pour {self.nom} : {loyer} €")
            return loyer
        return loyer_de_base

    def est_proprietaire(self, joueur) -> bool:
        """Vérifie si le joueur est le propriétaire de la propriété."""
        return self.proprietaire == joueur
    
    def __str__(self) -> str:
        return f"{self.nom} - Prix d'achats: {self.prix_achats} $ - Propriétaire: {self.proprietaire.nom if self.proprietaire else 'aucun'}"

p = Propriete(400, "rue de la paix")

print(p)