import random
import time

print('vou pensar em um numero entre 0 e 5, temte advinhar')
print('='*20)
l = random.randint(0, 5)
numero = int(input('digite um numero:'))
print(' Processando.....')
time.sleep(3)
if numero == l:
    print('parabens! voce acertou')
else:
    print('Ganhei, eu pensei no numero \033[1;31m{}\033[m e nao no \033[1;34m{}\033[m'.format(l, numero))



