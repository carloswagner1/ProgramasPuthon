#variáveis
maior = 0
#entrada
num = int(input("Informe um número: "))
#processamento
while num != 0:
    if num > maior:
        maior = num
    num = int(input("Informe um número: "))
print("O maior número é {0}".format(maior))