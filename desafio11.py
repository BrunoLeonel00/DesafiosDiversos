parede = float(input('digite a largura da parede:'))
altura = float(input('agora digite sua altura:'))
l = parede * altura
m = l / 2
print('Sua parede tem a dimençao de \033[1;37m{}\033[m X \033[1;37m{}\033[m e sua area é igual a \033[4;31m{}\033[mm.'.format(parede, altura, l))
print('Para pintar essa parede voce precissara de \033[1;34m{}\033[mL de tinta'.format(m))
