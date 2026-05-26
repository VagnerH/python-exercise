a = int(input('digite um numero '))
b = int(input('digite outro numero '))
if a > b:
    print('{}, é maior que ,{}'.format(a,b))
elif a < b:
    print('{}, é maior que ,{}'.format(b,a))
else:
    print('são do mesmo tamanho')