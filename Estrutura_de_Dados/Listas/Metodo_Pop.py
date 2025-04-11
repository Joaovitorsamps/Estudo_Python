#O método pop retira sempre o último elemento da lista
#Listas por padrão são organizadas como pilhas

numeros = [1, 2, 3, 4, 5, 6]

print(numeros.pop()) #6
print(numeros.pop()) #5
print(numeros.pop(0)) #1
print(numeros.pop(-2)) #3
print(numeros) # [2, 4]