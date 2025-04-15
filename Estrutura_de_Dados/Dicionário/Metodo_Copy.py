# Criando um dicionário original
dicionario_original = {
    'nome': 'Alice',
    'idade': 30,
    'habilidades': ['Python', 'Java', 'C++']
}

# Usando o método copy() para criar uma cópia do dicionário
dicionario_copia = dicionario_original.copy()

# Exibindo os dicionários
print("Dicionário Original:", dicionario_original)
print("Cópia do Dicionário:", dicionario_copia)

# Modificando a cópia
dicionario_copia['idade'] = 31
dicionario_copia['habilidades'].append('JavaScript')

# Exibindo os dicionários após a modificação
print("\nApós modificar a cópia:")
print("Dicionário Original:", dicionario_original)
print("Cópia do Dicionário:", dicionario_copia)