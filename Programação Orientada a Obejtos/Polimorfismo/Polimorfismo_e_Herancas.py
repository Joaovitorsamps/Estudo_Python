# Classe base: Passaro
# Ela define um comportamento genérico: voar()
class Passaro:
    def voar(self):
        print("Voando...")  # comportamento padrão

# Subclasse: Pardal
# Herda de Passaro e reimplementa o método voar()
class Pardal(Passaro):
    def voar(self):
        # Chama o método voar() da classe pai usando super()
        return super().voar()

# Subclasse: Avestruz
# Também herda de Passaro, mas sobrescreve o método voar com outro comportamento
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")  # comportamento específico

# Função que recebe qualquer objeto com o método voar()
def plano_voo(obj):
    obj.voar()  # chamada polimórfica

# Instanciação das subclasses
p1 = Pardal()
p2 = Avestruz()

# Chamadas usando a mesma função, mas comportamentos diferentes
plano_voo(p1)  # Saída: Voando...
plano_voo(p2)  # Saída: Avestruz não voa
