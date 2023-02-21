from math import sin, cos, tan, radians
angulo = float(input('digite um angulo:'))
seno = sin(radians(angulo))
print('O angulo de \033[1;34m{:.2f}\033[m tem o SENO igual a \033[1;34m{:.2f}\033[m'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('o angulo de \033[1;31m{:.2f}\033[m tem o COSSENO igual a \033[1;31m{:.2f}\033[m'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de \033[1;35m{:.2f}\033[m tem o TANGENTE igual a \033[1;35m{:.2f}\033[m'.format(angulo, tangente))






