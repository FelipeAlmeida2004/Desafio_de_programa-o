import math
from typing import List

s = str(input("Digite uma frase: "))
tam = len(s.strip()) - s.count(' ')
grid = round(math.sqrt(tam))
matriz_p =[s]
matriz_l = []
aux = 0
linha = []

for palavra in matriz_p:
    for i in palavra:
        linha.append(i)
        if i == " ":
            linha.remove(i)

            for j in range(grid):
                linha_add = []
                for k in range(grid):
                    linha_add.append(linha)


            matriz_l.append(linha_add)
print(matriz_l)


