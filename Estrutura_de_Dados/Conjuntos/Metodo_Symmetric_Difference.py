#Este método retorna apenas aquilo que é único de cada conjunto

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

diferenca_simetrica_ab = conjunto_a.symmetric_difference(conjunto_b)

print(diferenca_simetrica_ab)