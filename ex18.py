import math
angulo = int(input('digite um angulo '))
radiano = math.radians(angulo)
seno = math.sin(radiano)
coseno = math.cos(radiano)
tangente = math.tan(radiano)
print('do angulo {}% o seno é {:.2f} o cosseno é {:.2f} e a tangente é {:.2f}'.format(angulo, seno, coseno, tangente))