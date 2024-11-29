from terrain import terrain
from case import Case

class Plateau: 
    def __init__(self) -> None:
        self.plateau = []
        for t in terrain:
            self.plateau.append(Case(t, len(self.plateau)))  
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __repr__(self) -> str:
        message = "Plateau : "
        message += ", ".join(str(c) for c in self.plateau)  
        return message
    

plateau = Plateau()
