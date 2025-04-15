#Função {}.update tem de ser realizada fora do print, caso contrário retornará "none"
#Utilizada para atualizar completamente dicionário
#Caso a chave exista, ele atualizará conforme o que for declarado.
#Caso a chave não exista ele criará uma nova para atender ao que foi declarado

contatos = {
    "joaovitorsamps@hotmail.com": {"nome": "João Sampaio", "telefone": "92 98819-4669"}
}

# Atualiza os dados (sem print)
contatos.update({"joaovitorsamps@hotmail.com": {"nome": "João", "telefone": "92 98819-4669"}})
contatos.update({"layanachaves@gmail.com": {"nome": "Layana Chaves", "telefone": "xxxxx-xxxx"}})

print(contatos)