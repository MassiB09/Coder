lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []
i = 0

for elemento_1 in lista_1:
    for elemento_2 in lista_2:
        if elemento_1 == elemento_2:
            lista_3.append(elemento_1)
            break
print(lista_3)

lista_nueva = []

for element in lista_3:
    if element not in lista_nueva:
        lista_nueva.append(element)

print(lista_nueva)