distancia = float(input('Digite a distância da viagem desejada:'))
multa1 = 0.50 * distancia
multa2 = 0.45 * distancia
if distancia <= 200:
    print('Voce tera que pagar R$\033[1;34m{:.2f}\033[m, por essa viagem'.format(multa1))
else:
    print('voce tera que pagar R$\033[1;37m{:.2f}\033[m, por essa viagem0'.format(multa2))
print('Obrigado por escolher os nossos serviços, volte sempre')
