temperatura = float(input('Informe a temperatura atual em C:'))
F = temperatura * 1.8 + 32
print('A temperatura de \033[1;35m{}\033[mC, corresponde a \033[1;35m{:.1f}\033[mF!'.format(temperatura, F))
