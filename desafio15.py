dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos Kms rodados?'))
aluguel = (dias * 60) + (km * 0.15)
print('o total a pagar é de R$\033[1;34m{:.2f}\033[m'.format(aluguel))
