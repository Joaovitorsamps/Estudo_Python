class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, Pelagem, **kw):
        self.pelagem = Pelagem  
        
        #Para chamar o construtor pai, utiliza-se o "super()"
        super().__init__(**kw) 

class Ave(Animal):
    def __init__(self, cor_das_penas, cor_do_bico, **kw):
        self.cor_das_penas = cor_das_penas
        self.cor_do_bico = cor_do_bico
        
        #também pode ser escrito da seguinte forma: super().__init__(numero_patas=kw["numero_patas"])
        #Ao utilizar **kw, qualquer argumento adicionado na classe mãe sera utilizado automaticametne na filha
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Ornintorrinco(Mamifero, Ave):
    def __init__(self, Pelagem, cor_do_bico, **kw):
        super().__init__(Pelagem = Pelagem, cor_do_bico = cor_do_bico, **kw)
        print(Ornintorrinco.__mro__)

gato = Gato(numero_patas=4, Pelagem="Preto")
print(gato)

ornintorrinco = Ornintorrinco (numero_patas=4, Pelagem="Azul", cor_do_bico="Amarelo", cor_das_penas="NULL")
print(ornintorrinco)