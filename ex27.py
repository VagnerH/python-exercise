nome = str(input('digite seu nome: ')).strip()
primeironome = nome.split()[0]
ultimonome = nome.split()[-1]
print('seu primeiro nome é {} e seu ultimo é {}'.format(primeironome,ultimonome))