#Às vezes é necessário saber qual é o índice do objeto dentro do 
#laço for. Para isso podemos usar a função enumerate

carros = {"gol", "celta"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

linguagens = {"Java", "Python", "JavaScript", "Java", "Python"}

for indice, linguagem in enumerate(linguagens):
    print(f"{indice}: {linguagem}")

#Utilizando o enumerate e o for é possível retornar a sequência exata declarada