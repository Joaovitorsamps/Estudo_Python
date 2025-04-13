#Conjuntos em Python não suportam index
#Necessário converter o set em uma lista

numeros = {1,2,3,4}

numeros = list(numeros)

print(numeros[0])