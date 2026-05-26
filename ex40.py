n1 = float(input('qual foi sua primeira nota '))
n2 = float(input('qual foi sua segunda nota '))
media = (n1 + n2) / 2
print(media)
if media >= 7.0:
    print('aprovado')
elif media < 5:
    print('reprovado')
else:
    print('recuperação')