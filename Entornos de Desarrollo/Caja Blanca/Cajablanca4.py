a = list()
while True:
    size = int(input('Vamos a crear un array con valores consecutivos. '
                     'Dame la longitud del array (entero positivo): '))
    if size > 0:
        break
for i in range(size):
    a.append(i)
print('Ahora vamos a modificar el array')
while True:
    while True:
        posicion = int(input('Dame un elemento entre uno y' + str(size) + ':'))
        if posicion > 0 and posicion < size:
            break
    valor = int(input('Dame un valor para introducir en la posición' + str(posicion) + 'del array: '))
    a[posicion - 1] = valor
    respuesta = input('¿Quieres modificar otro valor? (s/n) ')
    if respuesta == 'n':
        break
for i in range(size):
    print('a[' + str(i) + '] = ' + str(a[i]))
