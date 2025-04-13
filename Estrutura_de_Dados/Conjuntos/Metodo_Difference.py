#Metodo {}.difference filtra apenas a parte pertencente a 
#determinado conjunto, ou seja, a parte que tem em um e não tem no outro

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

pertencente_a = conjunto_a.difference(conjunto_b)
pertencente_b = conjunto_b.difference(conjunto_a)

print(pertencente_a)
print(pertencente_b)