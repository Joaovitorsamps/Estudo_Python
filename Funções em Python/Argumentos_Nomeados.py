#Funções tambem podem ser chamadas usando argumentos nomeados da forma chave=valor
def salvar_carro(marca, modelo, ano, placa):
    #salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano = 1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
#Os asterísticos "**" informam que estou passando um dicionário para a função