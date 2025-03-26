nome = "JoãO"
print(" ")
print("------")
print(nome.upper())
print("------")
print(nome.lower())
print("------")
print(nome.title())
print("------")

texto = "         olá mundo !     "

print("------") 
print(texto + ".")
print("------")
print(texto.strip() + ".")
print("------")
print(texto.lstrip() + ".")
print("------")
print(texto.rstrip() + ".")
print("------")

menu = "Python"

print("------")
print("###" + menu + "###")
print("------")
print(menu.center(14))
print("------")
print(menu.center(14, "#"))
print("------")
print("P-y-t-h-o-n")
print("------")
for letra in menu:
    print(letra, end="-")
print(" ")
print("------")
print("-".join(menu))