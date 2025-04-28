from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    
class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligada")
        
    def desligar(self):
        print("Desligada")
