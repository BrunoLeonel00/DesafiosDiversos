from random import choice
print('SORTEIO')
a = str(input('participante 1:'))
b = str(input('participante 2:'))
c = str(input('participante 3:'))
d = str(input('participante 4:'))
lista = a, b, c, d
print(' o sorteado da vez é \033[1;35m{}\033[m'.format(choice(lista)))

