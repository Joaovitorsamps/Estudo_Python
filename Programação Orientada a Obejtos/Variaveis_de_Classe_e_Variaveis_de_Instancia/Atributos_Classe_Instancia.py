class Estudante:
    #Variáveis de Classe sõo declaradas após a inicialização da Class
    faculdade = "FAMETRO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def curso(self):
        # Salvando os dados no próprio objeto usando self
        self.area = input("\nQual a área de atuação? ")
        self.nome_curso = input("Qual o curso? ")
        self.quantidade_de_periodos = int(input("Quantos períodos tem seu curso? "))

    def __str__(self) -> str:
        return f"""
===============================================
{self.nome} - {self.matricula} - {self.faculdade}
===============================================
Área do curso: {self.area}
------------------------------------------------
Curso: {self.nome_curso}
------------------------------------------------
Períodos: {self.quantidade_de_periodos}
------------------------------------------------
"""

aluno1 = Estudante("João", 12345)
aluno1.curso()
print(aluno1)
