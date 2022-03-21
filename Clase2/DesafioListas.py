lista1 = [1, 12, 123]
lista2 = ['bye', 'ciao', 'agur', 'adieu']
lista1.append(1234)
lista1.append('hola')
lista3 = lista1         #Se puede usar lista3 = lista1[:4] y funciona igual
lista3.pop(-1)
print(lista3)
lista5 = lista1 + lista2
print(lista5)