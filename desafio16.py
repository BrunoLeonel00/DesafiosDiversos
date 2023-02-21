'''from math import trunc
num = float(input('digite um numero:'))
print('o numero {} tem a parte inteira igual a {}'.format(num, trunc(num)))'''

num = float(input('digite um numero:'))
print('o valor digitado foi  \033[1;36m{}\033[m e sua parte inteira é igual a \033[1;36m{}\033[m'.format(num, int(num)))

