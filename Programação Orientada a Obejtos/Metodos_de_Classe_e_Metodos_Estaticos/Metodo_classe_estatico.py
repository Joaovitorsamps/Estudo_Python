class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome 
        self.idade = idade
        
    #Transforma a função em um método de classe e no lugar do self se utiliza cls
    @classmethod
    def criar_data_de_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return Pessoa(nome, idade)
    
    
    @staticmethod
    def e_maior_idade(idade):
        return idade>= 18
    
pessoa1 = Pessoa.criar_data_de_nascimento(2002, 11, 3, "João")
print(pessoa1.nome, pessoa1.idade)

print(Pessoa.e_maior_idade(20))
print(Pessoa.e_maior_idade(17))