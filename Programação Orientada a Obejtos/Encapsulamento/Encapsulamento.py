#Variáveis ou métodos começados com _ já se é esperado que não pode manipulat a variável ou método

class Conta:
    def __init__(self, numero_agencia, saldo):
        self._saldo = saldo
        self.numero_agencia = numero_agencia
    
    def depositar(self, valor):
        self._saldo += valor
    
    def sacar(self, valor):
        self._saldo -= valor
        
    def mostrar_saldo(self):
        return self._saldo
    
conta = Conta("0001", 50)
conta.depositar(100)
print(conta.mostrar_saldo())