numeros = [1, 3, 6, 9]
numero = float(input('Ingrese un numero entero que este entre el 0 y el 9: '))
while  numero > 9 or numero < 0 or numero - int(numero) != 0:
    numero = float(input('Ingrese un numero entero que este entre el 0 y el 9: '))
else:
    if numero in numeros:
        print('El valor ingresado se encuentra en la lista')
    else:
        print('El valor ingresado no se encuentra en la lista')