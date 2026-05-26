salario = float(input('digite seu salario: R$ '))
if salario > 1250:
    aumento = salario * 0.10 + salario
else:
    aumento = salario * 0.15 + salario
print('quem ganhava {:.2f} vai começar a ganhar {:.2f}'.format(salario, aumento))