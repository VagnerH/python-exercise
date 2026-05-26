dias = int(input('quantos dias de aluguel? '))
km = float(input('quantos km rodados '))
pagamento = (dias * 60) + (km * 0.15)
print('o total a se pagar: R${:.2f}'.format(pagamento))