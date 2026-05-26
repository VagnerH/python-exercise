n = int(input('Digite um número para ver a sua tabuada: '))

print(
    '{} x 1  = {:2}\n'
    '{} x 2  = {:2}\n'
    '{} x 3  = {:2}\n'
    '{} x 4  = {:2}\n'
    '{} x 5  = {:2}\n'
    '{} x 6  = {:2}\n'
    '{} x 7  = {:2}\n'
    '{} x 8  = {:2}\n'
    '{} x 9  = {:2}\n'
    '{} x 10 = {:2}\n'.format(
        n, n*1,
           n, n*2,
           n, n*3,
           n, n*4,
           n, n*5,
           n, n*6,
           n, n*7,
           n, n*8,
           n, n*9,
           n, n*10
    )
)