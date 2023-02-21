a = int(input('digite o primeiro valor:'))
b = int(input('digite o segundo valor:'))
c = int(input('digite o terceiro valor:'))
# descobrindo o menor
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('o menor valor digitado foi \033[1;34m{}\033[m'.format(menor))
# descobrindo o maior
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi \033[1;31m{}\033[m '.format(maior))
