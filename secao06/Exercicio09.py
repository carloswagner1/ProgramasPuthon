#entradas
IndicePoluicao = float(input("Informe o indice de poluição: "))
#processamento e saída
if IndicePoluicao >= 0.3 and IndicePoluicao < 0.4:
    print("Suspender atividades do grupo 1.")
elif IndicePoluicao >= 0.4 and IndicePoluicao < 0.5:
    print("Suspender atividades dos grupos 1 e 2.")
elif IndicePoluicao >= 0.5:
    print("Suspender atividades de todos os grupos.")
else:
    print("Níveis aceitáveis de poluição.")    