contatos = {
    "joaovitorsamps@hotmail.com":{"nome": "João Sampaio", "telefone": "92 98819-4669"},
    "laynachaves2005@gmail.com":{"nome": "Layana Chavez", "telefone": "92 98819-4668"},
}

for chave, valor in contatos.items():
    print(chave, valor)

#Método {}.items retorna uma lista de tuplas e é o melhor método
#para iterar dicionários