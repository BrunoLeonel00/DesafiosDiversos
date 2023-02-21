n = int(input('digite um número:'))
m = n * 2
t = n * 3
r = n ** (1/2)
print('o dobro de \033[37m{}\033[m, vale \033[33m{}\033[m'.format(n, m))
print('o triplo de \033[35m{}\033[m, vale \033[31m{}\033[m'.format(n, t))
print('e a raiz quadrade de \033[34m{}\033[m, vale \033[31m{:.2f}\033[m'.format(n, r))
