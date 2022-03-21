numero1 = int(input('Ingrese un numero: '))
numero2 = int(input('Ingrese otro numero: '))
print('Opciones:\n1. Mostrar la suma\n2. Mostrar la resta\n3. Mostrar el producto\n4. Finalizar el programa\n\n')
opcion = int(input('Ingrese la opcion: '))

if opcion == 1:
    print(f'La suma de los numeros es: {numero1 + numero2}')
elif opcion == 2:
    print(f'La resta de los numeros es: {numero1 - numero2}')
elif opcion == 3:
    print(f'El producto de los numeros es: {numero1 * numero2}')
elif opcion == 4:
    print('No se realizaron operaciones')
else:
    print('La opcion ingresada no es valida')