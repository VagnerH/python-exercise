ano = int(input('em qual ano o atleta nasceu? '))
idade = 2026 - ano
print(idade)
if idade <= 9:
    print('atleta mirim')
elif 9 < idade <= 14:
    print('atleta infantil')
elif 14 < idade <= 19:
    print('atleta junior')
elif 19 < idade <= 20:
    print('atleta senior')
else:
    print('atleta master')
