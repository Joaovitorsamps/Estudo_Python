#Segunda forma de acessar e retornar valores do dicionário

contatos = {
    "joaovitorsamps@hotmail.com": {"nome": "João Vitor Sampaio", "contato": "92 98819-4669"}
}

print(contatos.get("chave")) #None
print(contatos.get("chave", {})) #{} é um valor default / dicionário vazio
print(contatos.get("joaovitorsamps@hotmail.com", {})) #"joaovitorsamps@hotmail.com": {"nome": "João Vitor Sampaio", "contato": "92 98819-4669"}
