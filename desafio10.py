n = float(input('quanto dinheiro vc tem na carteira? R$'))
c = n / 5.23
e = n / 5.57
l = n / 0.027
print('com R${:.2f} voce pode comprar US$\033[36m{:.2f}\033[m'.format(n, c))
print('\033[36m{:.2f}\033[m euros'.format(e))
print('e \033[36m{:.2f}\033[m pesos argentinos'.format(l))

