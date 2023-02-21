nome = str(input('Digite seu nome completo:')).strip()
n = nome.split()
print('muito prazer em te conhcer!')
print(' seu primeiro nome é \033[1;34m{}\033[m'.format(n[0]))
print(' seu ultimo nome é \033[1;31m{}\033[m'.format(n[len(n)-1]))


