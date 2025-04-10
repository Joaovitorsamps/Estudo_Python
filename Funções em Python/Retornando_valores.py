#Para retornar um valor, utilizamos a palavra reservada "return"
#Toda função em Python retorna "none" por padrão
#Em python uma função pode retornar mais de um valor
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def return_none():
    print("Olá, Mundo !")

print("\n", calcular_total([10, 20, 34])) #64
print("\n", retorna_antecessor_e_sucessor(10)) #(9, 11)
print("\n", return_none)