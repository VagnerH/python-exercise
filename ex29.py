velocidade = int(input('digite a velocidade do veiculo '))
if velocidade > 80:
    multa = float(velocidade - 80) * 7
    print('você foi multado, a multa custará R${:.2f}'.format(multa))
print('boa viagem')
