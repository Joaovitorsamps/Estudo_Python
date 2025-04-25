# Define uma classe chamada Foo
class Foo:
    def __init__(self, x=None):
        # Atributo "protegido" (convenção com _)
        self._x = x

    # ---------------------------------------------
    # @property transforma o método em um "atributo"
    # Agora você pode acessar foo.x ao invés de foo.x()
    # ---------------------------------------------
    @property
    def x(self):
        # Retorna o valor de _x, ou 0 se for None ou False
        return self._x or 0

    # ---------------------------------------------
    # @x.setter define o comportamento ao fazer foo.x = valor
    # Esse método não retorna nada, apenas altera _x
    # ---------------------------------------------
    @x.setter
    def x(self, valor):
        # Soma o valor recebido ao valor atual de _x
        self._x += valor

    # ---------------------------------------------
    # @x.deleter define o que acontece quando você faz: del foo.x
    # Aqui, simplesmente zera o valor de _x
    # ---------------------------------------------
    @x.deleter
    def x(self):
        self._x = 0

# Cria uma instância da classe Foo com _x = 10
foo = Foo(10)

# Usa o deleter para "deletar" x, mas na prática isso só zera _x
del foo.x  # agora foo._x = 0

# Acessa foo.x (via @property), imprime: 0
print(foo.x)

# Usa o setter para somar 10 ao valor atual (_x += 10)
foo.x = 10  # agora foo._x = 10

# Imprime foo.x novamente (via getter)
print(foo.x)
