print('-=-'*15)
print('Analisador de triangulo'.center(43))
print('-=-'*15)
reta1 = float(input('digite o primeiro numero '))
reta2 = float(input('digite o segundo numero '))
reta3 = float(input('digite o terceiro numero '))
if reta1 + reta2 > reta3 and reta3 + reta2 > reta1 and reta1 + reta3 > reta2:
    print('os segmentos podem formar um triangulo')
else:
    print('os segmentos não podem formar um triangulo')