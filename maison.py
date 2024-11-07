class maison():
    def __init__(self, cout : int, loyer : int):
        self.cout = cout
        self.loyer = loyer
        self.nb_maison = 0
    
    def nb_de_maison(self) -> int:
        return self.nb_maison
    
    def est_hotel(self) -> bool:
        return self.nb_maison == 5