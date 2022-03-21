cadena = 'acitametaM ,5.8 ,otipeP ordeP'
cadena_volteada = cadena[::-1] #Doy vuelta la cadena
#print(cadena_volteada)
nombre_alumno = cadena_volteada[0:12] #Extraigo el nombre y apellido
#print(nombre_alumno)
nota = cadena_volteada[14:17] #La nota
#print(nota)
materia = cadena_volteada[19:]  #La materia
#print(materia)
cadena_formateada = nombre_alumno + ' ha sacado un ' + nota + ' en ' + materia #Formateo la cadena
print(cadena_formateada)