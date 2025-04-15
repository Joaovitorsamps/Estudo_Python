#Exclui uma chave do dicionário e caso ele não encontre a chave, pode retornar um valor default

contatos = {
    "joaovitorsamps@hotmail.com":{"nome": "João Sampaio", "telefone": "92 98819-4669"}
}

print(contatos.pop("joaovitorsamps@hotmail.com"))

print(contatos.pop("joaovitorsamps@hotmail.com", "Não encontrado"))