#O "*" define que tudo seja nomeado, cada argumetno
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo = "Palio", ano = 1999, placa = "ABC-1234", marca = "Fiat", 
            motor = "1.0", combustivel = "Diesel")