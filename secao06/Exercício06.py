#entradas
Nome = input("Informe o Nome do Funcionário: ")
HorasTrabalhadas = int(input("Informe a quantidade de horas trabalhadas: "))
#processamento
if HorasTrabalhadas > 50:
    HorasExtras = (HorasTrabalhadas - 50) * 20.00
    SalarioMensal = 50 * 10.00
    print("Funcionário: {0}".format(Nome))
    print("Salário: R$ {0:.2f}".format(SalarioMensal))
    print("Horas Extras R$ {0:.2f}".format(HorasExtras))
if HorasTrabalhadas < 50:
    SalarioMensal = HorasTrabalhadas * 10.00
    print("Funcionário: {0}".format(Nome))
    print("Salário: R$ {0:.2f}".format(SalarioMensal))    
    