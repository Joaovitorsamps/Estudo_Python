#Se um conjunto é subconjunto de outro quer dizer que todos os
#elementos de A pertencem B

conjunto_a = {1,2,3,4}
conjunto_b = {1,2,3,4,5,6}

pertence_ab = conjunto_a.issubset(conjunto_b)
pertence_ba = conjunto_b.issubset(conjunto_a)

print(pertence_ab) #True
print(pertence_ba) #False