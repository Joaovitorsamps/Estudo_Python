tupla =  ("p", "y", "t", "h", "o", "n",)
#         0    1    2    3    4    5
tupla[2:] #["t", "h", "o", "n"] 

tupla[:2] #["p", "y"] Nota: ":2" faz ele parar antes do item 2, ou seja, não imprime o "t"

tupla[1:3] #["y", "t"]

tupla[0:3:2] #["p", "t"] Nota: Há a contagem a partir do 0 e o ":2" faz ele pular de 2 em 2 elementos até a parada declarda 

tupla[::] #["p", "y", "t", "h", "o", "n"]

tupla[::-1]#["n", "o", "h", "t", "y", "p"]