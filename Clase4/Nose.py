tu_edad = input(' ingresa tu edad ')

  

#acá comiensza el filtrado para reconocer si nos están poniendo un caracter vacio

if tu_edad == '':

  tu_edad = input(' ingresa nuevamente edad ')

  

#si es así nos va a volver a pedir que ingresemos la edad.

edad_transformada = int(tu_edad)

  

#una vez ingresada la edad entonces las transformammos a entero para que pueda averiguar si es menor o mayor

print(edad_transformada)

  

if edad_transformada >= 18:

  print('bienvenido')

else:

  print('sos un purrete ')