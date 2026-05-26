distancia = int(input('digite quantos kilometros tem sua viagem '))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print('a passagem da sua viagem de {}km custará R${:.2f}'.format(distancia,passagem))
