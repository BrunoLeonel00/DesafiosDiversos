preco = float(input('Digite o preço do produto para saber o seu desconto: R$'))
d = 5 / 100 * preco
n = preco - d
print('O produto que custava R${}, na promaçao com desconto de 5%, passou a custar R$\033[35m{:.2f}\033[m'.format(preco, n))

