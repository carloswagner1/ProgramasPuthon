#entradas
Altura = float(input("Informe a sua altura: "))
sexo = input("Informe o sexo (m/f): ")
#processamento
if sexo.lower() == 'm':
    PesoIdeal = (72.7 * Altura) -58
elif sexo.lower() == 'f':
    PesoIdeal = (62.1 * Altura) - 44.7
else:
    PesoIdeal = 0
    print("Sexo não reconhecido.")
print("O peso ideal é {0:.2f} Kg".format(PesoIdeal))
    