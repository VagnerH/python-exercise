import random
numero = int(input('adivinhe o numero '))
numerocerto = random.choice([0,1,2,3,4,5])
if numero == numerocerto:
    print('parabéns!! você acertou o numero')
else:
    print('vixi, você errou o numero. O numero era {}'.format(numerocerto))