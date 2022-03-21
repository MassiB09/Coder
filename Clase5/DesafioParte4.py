iteraciones = int(input('Cuantos numeros quiere digitar: '))
suma = 0
for numero in range(iteraciones):
    suma += int(input('Ingrese un numero: '))
print(suma / iteraciones)