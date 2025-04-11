#Metodo [].sort faz a ordenação da lista

numero = [1,2,3,4,5] # 5, 4, 3, 2, 1
print(numero.sort())

numero = [1,2,3,4,5]
print(numero.sort(reverse = True)) # 1, 2, 3, 4, 5

numeros = ["1A1234","2B","3","4D12","5E1234"]
print(numeros.sort(key=lambda x: len(x))) # 3, 2b, 4D12, 1A1234, 5E1234 
#len() só funciona com sequências de string
#A função anônima Lambda faz a contagem do tamanho da string e imprime de acordo com ele

numeros = ["1A1234","2B","3","4D12","5E1234"]
print(numeros.sort(key=lambda x: len(x), reverse = True)) # 1A1234, 5E1234, 4D12, 2B, 3