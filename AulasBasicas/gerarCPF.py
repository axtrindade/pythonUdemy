from random import  randint
numero = str(randint(100000000, 999999999))

contador = 0
contador2 = 0
somatotal = 0
somatotal2 = 0
cpfnew = numero

for i in range(10, 1, -1):

    num_cpf = cpfnew[contador]
    contador+=1
    soma = int(num_cpf) * i
    somatotal += soma

novoDigito = 11 - (somatotal % 11)
if novoDigito > 9:
    novoDigito = 0
cpfnew += str(novoDigito)


for j in range(11, 1, -1):
    num_cpf2 = cpfnew[contador2]
    contador2+=1
    soma2 = int(num_cpf2)*j
    somatotal2 += soma2

novoDigito2 = 11 - (somatotal2 % 11)
if novoDigito2 > 9:
    novoDigito2 = 0
cpfnew+= str(novoDigito2)

print(cpfnew)