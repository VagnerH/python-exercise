ano = int(input('digite o ano do seu nascimento '))
idade = 2026 - ano
falta = 18 - idade
passou = idade - 18
if idade < 18:
    print('ainda precisa se alistar, falta {} anos para o alistamento'.format(falta))
elif idade == 18:
    print('esta na hora de se alistar')
else:
    print('ja passou da hora de se alistar, atrasou {} anos'.format(passou))
