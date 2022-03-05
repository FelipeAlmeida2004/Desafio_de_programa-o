
n = [1, 5, 3, 4, 2]
x = int(input("Digite o número da diferença desejada: "))
i = 0
cont = 0
for i in n:
    for j in n:
     dif = abs(i - j)
     if(dif == x):
        if(i-j == dif):
            pares = [i,j]
            cont = cont + 1

print("O número de pares são: ",cont)


