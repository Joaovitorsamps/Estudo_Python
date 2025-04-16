from datetime import datetime as dt, timedelta

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60

def solicitar_tipo_carro():
    entrada_de_dados = input("""
                   Digite:
                   --------------------
                   P - Carros pequenos
                   M - Carros médios
                   G - Carros grandes
                   S - Sair
                   --------------------
                   """)
    return entrada_de_dados[0].upper() if entrada_de_dados else ""

data_atual = dt.now()
informacao_letra = solicitar_tipo_carro()

while informacao_letra != "S":
    tempo_estimado = None

    match informacao_letra:
        case "P":
            tempo_estimado = tempo_pequeno
        case "M":
            tempo_estimado = tempo_medio
        case "G":
            tempo_estimado = tempo_grande
        case _:
            print("Insira uma opção válida")

    if tempo_estimado is not None:
        data_estimada = data_atual + timedelta(minutes=tempo_estimado)
        print(f'O carro chegou: {data_atual} e ficará pronto às {data_estimada}')

    informacao_letra = solicitar_tipo_carro()
