#A "/" obriga que a declaração seja feita apenas de acordo com a posição do argumento
#Os parâmetros após a barra "/" podem ser nomeados ou apenas pela posição
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Uno", 1999, "ABC-1234", marca = "Volkswagen", motor = "1.0",
            combustivel = "Gasolina") #Válido
