nome = "João"
idade = 22
profissao = "Data Analyst"
linguagem = "Python"

pessoa = {"nome1": "Layana", "idade1": 19, "profissao1": "Fisioterapeuta", "especializacao": "Neuroterapia"} #Forma de definir um dicionário em Python

print("\nOlá, me chamo {}, temho {} anos e atualmente sou {} especializado em trabalhar com {}".format(nome, idade, profissao, linguagem))

print("\nOlá, me chamo {3}, temho {2} anos e atualmente sou {1} especializado em trabalhar com {0}".format(linguagem, profissao, idade, nome))

print("\nOlá, me chamo {nome}, temho {idade} anos e atualmente sou {profissao} especializado em trabalhar com {linguagem}".format(nome = nome, idade = idade, profissao = profissao, linguagem = linguagem))

print("\nOlá, me chamo {nome1}, temho {idade1} anos e atualmente sou {profissao1} especializado em trabalhar com {especializacao}".format(**pessoa))
#No último modelo é definido um dicionário para poder chamar as variáveis na função print

#O método format permite organizar como e em que ordem as varáveis serão chamadas para o programa, no entanto também esta caindo em desuso