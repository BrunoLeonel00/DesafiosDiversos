#'''Escreva um programa para aprovar o emprestimo bancario na compra de um casa.
# pergunte o valor da cada, o salário do comprador e em quantos anos ele vai pagar.
# A prestaçao nao pode exceder o valor de 30% do salario, se nao o emprestimo sera negado'''

casa = float(input('qual o valo da casa que deseja comprar? R$'))
salario = float(input('Digite seu salario atual: R$'))
anos = int(input('quantos anos de finaciamento:'))
prestaçao = (casa / anos) / 12
porcento = (30 / 100) * salario
if prestaçao < porcento:
    print('Para pagar uma casa de {} em {} anos, a prestaçao sera de {:.2f}'.format(casa, anos, prestaçao))
    print('Tudo certo, podemos fazer o emprestimo')
elif prestaçao >= porcento:
    print('Para pagar uma casa de R${} em {} anos, a prestação sera de {:.2f} '.format(casa, anos, prestaçao))
    print('Empréstimo NEGADO!')

