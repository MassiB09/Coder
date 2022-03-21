nota_1 = int(input('ingrese la nota de su primer examen: '))     #Pido la primer nota y la convierto en un enterto
nota_2 = int(input('ingrese la nota de su segundo examen: '))    #Pido la segunda nota y la convierto en un entero
nota_final = (nota_1 * 40 + nota_2 * 60) / 100                   #Calculo la nota final en base a lo que se pide
print(f'La nota final es: {nota_final}')                                           #Imprimo por pantalla la nota final