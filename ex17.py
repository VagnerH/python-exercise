import math
cateto1 = int(input('qual o tamanho do primeiro cateto? '))
cateto2 = int(input('qual o tamanho do segundo cateto? '))
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
print('a hipotenusa vale {:.2f}'.format(hipotenusa))