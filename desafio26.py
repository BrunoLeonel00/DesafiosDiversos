nome = str(input('digite seu nome:')).strip().lower()
print('A letra A aparece \033[1;32m{}\033[m vezes ma frase'.format(nome.count('a')))
print('A primeira letra A aparece na posiçao \033[1;33m{}\033[m'.format(nome.find('a')+1))
print('A ultima letra A aparece na posiçao \033[1;37m{}\033[m'.format(nome.rfind('a')+1))
