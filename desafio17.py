from math import sqrt
CO = int(input('cateto oposto:'))
CA = int(input('cateto adjascente:'))
Hi = (CO ** 2) + (CA ** 2)
print('o valor da hipotenusa é igual a \033[1;32m{:.2f}\033[m'.format(sqrt(Hi)))



