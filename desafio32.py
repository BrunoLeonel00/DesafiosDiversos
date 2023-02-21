
ano = int(input('Digite um ano para saber se ele é ou nao é bissexto, se quiser saber sobre o ano atual digite 0:'))
n = ano % 4
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano de \033[1;31m{}\033[m é um ano bissexto'.format(ano))
else:
    print('o ano de \033[1;32m{}\033[m nao é um ano bissexto'.format(ano))
