frase = str(input('digite o seu nome completo:')).strip()
n = frase.upper()
b = frase.lower()
c = len(frase[:5])
d = frase[:5]
print('analisando seu nome...')
print('Seu nome em maiusculo é \033[1;36m{}\033[m'.format(n))
print('Seu nome em minusculo é \033[1;31m{}\033[m'.format(b))
print('Seu nome tem ao todo \033[1;32m{}\033[m letras'.format(len(frase) - frase.count(' ')))
separa = frase.split()
print('Seu primeiro nome é \033[1;31m{}\033[m e ele tem \033[1;31m{}\033[m letras'.format(separa[0], len(separa[0])))
