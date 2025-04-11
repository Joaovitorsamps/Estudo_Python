numeros = [1, 30, 22, 15, 12, 11, 50, 100]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

#2° Método

impares = [numero for numero in numeros if numero % 2 != 0]

print(impares)