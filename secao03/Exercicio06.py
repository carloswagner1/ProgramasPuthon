#entradas
SalarioHora = float(input("Informe o salário hora: "))
HorasTrabalhadas = int(input("Informe a quantidade de horas trabalhadas: "))
#processamentos
SalarioMensal = SalarioHora * HorasTrabalhadas
#saida
print("O salário mensal é R$ {0:.2f}".format(SalarioMensal))