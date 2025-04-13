#O contrário do método issubset, ele identifica quando um conjunto
#não pertende a outro

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5,6}

pertence_ab = conjunto_a.issuperset(conjunto_b)
pertence_ba = conjunto_b.issuperset(conjunto_a)

print(pertence_ab) #False
print(pertence_ba) #True