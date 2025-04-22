# __del__ é umm método destrutor que é utilizado para
#eliminar instâncias(obejtos) e o sistema do Python
#gerencia a memória para evitar "lixo"

class cachorro:
    def __del__(self):
        print("Destruindo Instância")
        
c = cachorro()
del c