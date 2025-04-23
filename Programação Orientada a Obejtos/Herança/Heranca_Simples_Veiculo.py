class Veiculo:
    def __init__(self, marca, cor, motor, numero_de_rodas, placa):
        self.marca = marca
        self.cor = cor
        self.motor = motor
        self.numero_de_rodas = numero_de_rodas
        self.placa = placa

    def ligar_motor(self):
        print(f"Motor {self.motor:.2f} ligado. Ronco genérico.")

    def __str__(self):
        return (f"Marca: {self.marca}, Cor: {self.cor}, Motor: {self.motor}, "
                f"Rodas: {self.numero_de_rodas}, Placa: {self.placa}")

class Motocicleta(Veiculo):
    def ligar_motor(self):
        if self.motor < 2.0:
            print(f"Ronco {self.motor:.2f}: RandandanRandandan...")
        else:
            print(f"Ronco {self.motor:.2f}: RAMDAMDAMDAM...")

class Carro(Veiculo):
    def ligar_motor(self):
        if self.motor < 2.0:
            print(f"Ronco {self.motor:.2f}: VrumVrum...")
        else:
            print(f"Ronco {self.motor:.2f}: VRUMMMMMMMM...")


class Caminhao(Veiculo):
    def ligar_motor(self):
        print(f"Ronco {self.motor:.2f}: TRONNNNNNNNNNNNNNNNNNNNNNNN...")

moto1 = Motocicleta("Honda", "Preto e Branco", 2.0, 2, "ABC-1234")
print(moto1)
moto1.ligar_motor()

carro1 = Carro("Honda", "Preto", 1.6, 4, "CDE-4567")
print(carro1)
carro1.ligar_motor()

caminhao1 = Caminhao("Mercedez Benz", "Branco", 5.0, 6, "FGH-8901")
print(caminhao1)
caminhao1.ligar_motor()