vel = int(input('Bom dia, qual a velocidade atual do seu carro?'))
multa = (vel - 80) * 7
if vel <= 80:
    print('\033[1;34mMuito bem, dirija com segurança\033[m')
else:
    print('MULTADO!!! Você excedeu o limite de velocidade permitido de 80Km/h.\nVoce deve pagar uma multa de R$\033[1;36m{:.2f}\033[m'.format(multa))
    print('\033[1;31mTenha um bom dia e DIRIJA COM SEGURANÇA!!!!\033[m')
