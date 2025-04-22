class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
        print("PLIM PLIM...")
        
    def parar(self):
        print("Parando...")
        print("Bicicleta parada")
    
    def correr(self):
        print("Tectectectec...")
        
Bicicleta_1 = Bicicleta("vermelha", "Caloi", 2025, 1250.00) 