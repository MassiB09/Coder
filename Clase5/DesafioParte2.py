numero = int(input('Ingrese un numero impar: '))
while numero % 2 == 0:
    print('El numero ingresado no es impar\n')
    numero = int(input('Ingrese un numero impar: '))
else:
    print(f'El numero ingresado: "{numero}" es impar')