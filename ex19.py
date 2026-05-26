import random
aluno1 = str(input('digite o nome do aluno '))
aluno2 = str(input('digite o nome do segundo aluno '))
aluno3 = str(input('digite o nome do terceiro aluno '))
aluno4 = str(input('digite o nome do quarto aluno '))
lista = (aluno1,aluno2,aluno3,aluno4)
escolhido = random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))