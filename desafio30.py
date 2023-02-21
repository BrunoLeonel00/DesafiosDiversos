numero = int(input('digite um numero:'))
par = (numero % 2)

if par == 0:
    print('Seu numero \033[1;34m{}\033[m é PAR'.format(numero))
else:
    print('seu numero \033[1;31m{}\033[m é IMPAR'.format(numero))
