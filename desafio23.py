num = int(input('digite um numero:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(' analisando o numero \033[1;34m{}\033[m'.format(num))
print(' unidade: \033[1;36m{}\033[m'.format(u))
print('dezena: \033[1;35m{}\033[m'.format(d))
print('centena: \033[1;31m{}\033[m'.format(c))
print('milhar: \033[1;32m{}\033[m'.format(m))
