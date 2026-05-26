import random
grupo1 = str(input('digite o nome do primeiro grupo '))
grupo2 = str(input('digite o nome do primeiro grupo '))
grupo3 = str(input('digite o nome do primeiro grupo '))
grupo4 = str(input('digite o nome do primeiro grupo '))
lista = [grupo1, grupo2, grupo3, grupo4]
random.shuffle(lista)
print('a ordem de apresentação é: {}'.format(lista))