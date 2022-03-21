import sys

if len(sys.argv) == 3:
    print(f'Nota 1 es: {sys.argv[1]}\n\n')
    print(f'Nota 2 es: {sys.argv[2]}\n\n')
    if (int(sys.argv[1]) + int(sys.argv[2])) / 2 > 7.0: 
        print('Muy bien')
else:
    print('Faltan o sobran notas')