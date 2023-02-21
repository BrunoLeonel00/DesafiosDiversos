n = float(input('digite uma distancia em metros:'))
print(' a medida de 3.0m corresponde a:')
print('\033[1;31m{}km\033[m'.format(n / 1000))
print('\033[4;32m{}hm\033[m'.format(n / 100))
print('\033[7;33;34m{}\033[mdam'.format(n / 10))
print('\033[34m{}\033[mdm'.format(n * 10))
print('\033[1;35m{}cm\033[m'.format(n * 100))
print('\033[1;35;46m{}\033[mmm'.format(n * 1000))


