print('-=' * 20)
print('analisador de triangulos')
print('-=' * 20)
a = float(input('digite o primeiro segmento:'))
b = float(input('digite o segunfo segmento:'))
c = float(input('digite o terceiro segmento:'))
if a < b + c and b < a + c and c < a + b:
    print('\033[1;34msim, pode formar um triangulo\033[m')
else:
    print('\033[1;31m nao, nao podem formar um triangulo\033[m')






