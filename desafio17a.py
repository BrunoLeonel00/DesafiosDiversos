from math import hypot
Co = int(input('cateto oposto:'))
Ca = int(input('cateto adjascente:'))
print('a hipotenusa é igual a \033[1;35m{:.2f}\033[m'.format(hypot(Co, Ca)))
