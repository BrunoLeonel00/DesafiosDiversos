salario = float(input('digite seu salario: R$'))
if salario > 1250:
    novo = salario + (10 / 100 * salario)
    print('parabens, voce ganhou um aumento de 10%, seu salario vai ser \033[1;31m{}\033[m Reais'.format(novo))
if salario <= 1250:
    novo = salario + (15 / 100 * salario)
    print('parabens, voce ganhou um aumento de 15%, seu novo salario sera de \033[1;34m{}\033[m reais'.format(novo))
