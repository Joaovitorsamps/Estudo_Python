#Podemos combinar parâmetros obrigatórios com args e kwargs.
#Quando esses são definidos (*args e **kwargs)
#Recebe os valores como tupla e dicionário respectivamente

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of Python", "Beautiful is better than ugly.", author = "Tim Peter", ano = 1999)