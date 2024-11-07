class Propriete():
    def __init__(self,prix_achats : int, nom : str, valeur_hypoteque):
        self.prix_achats = prix_achats
        self.nom = nom
        self.valeur_hypoteque = valeur_hypoteque
        self.est_hypoteque : bool = False
        self.quartier = None
        self.proprietaire = None
    
    def achete(self, Joueur):
        pass
    
    def vendre(self, Joueur):
        pass
    
    def hypoteque(self):
        pass
    
    def liberer_hypoteque(self):
        pass
    
    def calalculer_loyer(self) -> int:
        pass
    
    def est_proprietaire(self):
        pass




