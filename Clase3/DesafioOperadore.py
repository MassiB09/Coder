expresiones = [
    False == True,
    10 >= 2 * 4,
    33 / 3 == 11,
    True > False,
    True * 5 == 2.5 * 2
]

respuestas = [
    False,
    True,
    True,
    True,
    True
]

print(f'Son las listas iguales?\n{expresiones == respuestas}')

#Otro desafio

expresiones = [
    not False,
    not True == False,
    not 3 == 5,
    33 / 3 == 11 and 5 > 2,
    True or False
    
]