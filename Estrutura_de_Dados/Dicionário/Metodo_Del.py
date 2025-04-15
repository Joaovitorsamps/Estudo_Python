#Outra maneira de retirar valores do dicionário

contatos = {
    "joaovitorsamps@hotmail.com":{"nome": "João Sampaio", "telefone": "92 98819-4669"},
    "laynachaves2005@gmail.com":{"nome": "Layana Chaves", "telefone": "92 98819-4668"},
}

print(contatos)

del contatos["joaovitorsamps@hotmail.com"]["telefone"]

print(contatos)

del contatos["laynachaves2005@gmail.com"]

print(contatos)

del contatos

print(contatos) #Agora retorná erro, pois o último del excluiu o dicionário
 