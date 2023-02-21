nome = str(input('Digite seu nome completo:')).strip()
print('seu nome tem silva? \033[1;31m{}\033[m'.format('silva' in nome.lower()))
