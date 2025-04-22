class Cachorro:
    def __init__(self, nome, raca, acordado = True):
        self.nome = nome
        self.raca = raca
        self.acordado = acordado
        
    def __del__(self):
        print("Removendo instância da classe.")
        
    def som(self):
        print("AUAUAUAUAUAUAU")
        
def criar_cahorro():
    c = Cachorro("Linda", "Dalmata", False)
    print(c.nome)
        
c = Cachorro("Bruce", "Bulldogue Inglês")
c.som()
criar_cahorro()