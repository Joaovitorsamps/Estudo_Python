#Serve para identificar quando conjuntos não tem interseção

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

nao_intersecao_ab = conjunto_a.isdisjoint(conjunto_b)
nao_intersecao_ac = conjunto_a.isdisjoint(conjunto_c)

print(nao_intersecao_ab) #True
print(nao_intersecao_ac) #False