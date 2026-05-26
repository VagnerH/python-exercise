valor = float(input('qual o valor da casa? '))
salario = float(input('qual sua renda salarial? '))
anos = int(input('em quantos anos você pretende pagar a casa? '))
anos = anos * 12
prestacao = valor / anos
porcentagemsalario = salario * 0.3
if porcentagemsalario < prestacao:
    print('Acesso negado')
else:
    print('Prestação concluída')