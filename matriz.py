# Definir la lista de listas
m = [[2, 5, 3],
     [6, 1, 8],
     [7, 5, 4]]

matriz = True

# Verificar si m es una matriz 
for listas in m:
    # Comprobar si es una matriz con el mismo número de elementos en cada sublista
    if len(listas) != len(m[0]):
        matriz = False 
        break

# Imprimir si no es una matriz
if matriz == False:
    print('M no es una matriz')
else:
    # Encontrar la fila con la mayor suma de elementos
    suma_maxima = sum(m[0])  # Inicializar la suma máxima con la primera fila
    fila_mas_alta = m[0]

    for lista in m:
        if sum(lista) > suma_maxima:
            suma_maxima = sum(lista)
            fila_mas_alta = lista

    print(f'La fila con la mayor suma de elementos es: {fila_mas_alta} con un total de {suma_maxima}')

    # encontrar la columna con mayor valor e imprimirla 
    columna_maxima = 0
    suma_maxima = 0
    for i in range(len(m)):
        columna = []
        suma_columna = 0
        for fila in m:
            suma_columna += fila[i]
            columna.append(fila[i])
        if suma_columna > suma_maxima:
            suma_maxima = suma_columna
            columna_maxima = columna[:]
    print(f'La columna mas grande es {columna_maxima} con un total de {suma_maxima}')

 