#Verifica se o item contem ou não no dicionário e retorna True ou False

contatos = {
    "joaovitorsamps@hotmail.com":{"nome": "João Sampaio", "telefone": "92 98819-4669"},
    "laynachaves2005@gmail.com":{"nome": "Layana Chaves", "telefone": "92 98819-4668"},
}

print("idade" in contatos["joaovitorsamps@hotmail.com"])  # False
print("nome" in contatos["laynachaves2005@gmail.com"])    # True