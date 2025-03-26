#def é a palavra chave em python que define o início de uma função
def exibir_mensagem():
    print("Olá Mundo!")
def exibir_mensagem1(nome): #Neste caso está definido o parâmetro "nome"
    print(f"seja bem vindo {nome}")
def exibir_mensagem2(nome = "Anônimo"):
    print(f"Seja bem vindo {nome}")

print("\n")

exibir_mensagem()
exibir_mensagem1(nome = "João")
exibir_mensagem2()
exibir_mensagem2(nome = "Layana")