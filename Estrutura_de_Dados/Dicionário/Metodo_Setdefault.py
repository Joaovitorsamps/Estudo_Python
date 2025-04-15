#Adiciona uma chave (caso ela não exista no dicionário) e o valor
#declarado na sequência (Valor é atribuido independente da cahve existir ou não)
#Ele sempre vai adicionar uma chave nova em caso de dicionário aninhados

contato = {"nome": "João Sampaio", "telefone": "92 98819-4669"}

print(contato.setdefault("nome", "Layana"))

print(contato.setdefault("idade", 22))

print(contato)

contatos = {
    "joaovitorsamps@hotmail.com":{"nome": "João Sampaio", "telefone": "92 98819-4669"}
}

#print(contatos.setdefault("joaovitorsamps@hotmail.com", "nome", "Layana"))
#ERROR DE SYNTAX

print(contatos.setdefault("nome", "Layana"))

print(contatos)