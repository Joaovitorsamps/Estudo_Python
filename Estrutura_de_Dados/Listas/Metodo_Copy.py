#Copia todos os elementos de uma lista, mas não faz delas iguais
#O que alterar em uma não interfere na outra

lista_1 = [1, "Python", [1,2,3,4,]]

lista_2 = lista_1.copy()

print(id(lista_1), id(lista_2)) #ID delas é diferente

lista_2[2] = "Mudança"

print(lista_1, "\n", lista_2)