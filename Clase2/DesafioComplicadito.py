matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
indice = 0 #Creo un indice para hacer mas expresivo mi programa
matriz[indice].append(sum(matriz[indice])) #Sumo los numeros de la matriz, luego ese resultado lo appendeo a la lista dentro de la matriz
matriz[indice + 1].append(sum(matriz[indice + 1])) 
matriz[indice + 2].append(sum(matriz[indice + 2]))
matriz[indice + 3].append(sum(matriz[indice + 3])) #Repito la logica 3 veces mas (Espero que esto se pueda optimizar con algun bucle en un futuro xd)
print(f'La nueva matriz es: {matriz}') #Muestro por pantalla la matriz ya modificada