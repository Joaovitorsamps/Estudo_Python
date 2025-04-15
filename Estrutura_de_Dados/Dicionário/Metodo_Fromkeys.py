#Cria chaves e para adicionar valor é necessário fechar colchetes, usar vírgula e passar o valor padrão desejado
#O método substitui chaves pré existentes

pessoa = dict(altura = 1.72)

print(pessoa)

pessoa = dict.fromkeys(["nome", "telefone"], "Desconhecido")

print(pessoa)