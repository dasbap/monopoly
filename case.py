class Case():
    def __init__(self, Case, position : int):
        self.case = Case
        self.nom = Case.nom
        self.position = position
    
    def __str__(self):
        return f"Case : {self.nom} (position : {self.position}"