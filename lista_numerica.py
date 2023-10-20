# crear una lista que contenga números
numeros = list(range(1,11))

#--- nueva lista con los números pares pero al reves
# crear lista con pares
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

nueva_lista = pares[::-1]

# bucle que recorra la lista numeros e imprima el cuadrado de cada número
for numero in numeros:
    print(numero**2)

# imprimir el número mas pequeño de la lista 
print(min(numeros))

#  lo mismo pero con el número mas alto
print(max(numeros))

# --- sumar todos los números de la lista con y sin bucle 
# con bucle 
suma = 0
for numero in numeros:
    suma += numero
print(f'el resultado de la suma de todos los números de la lista es {suma}')
# sin bucle 
print(f'suma dos: {sum(numeros)}')

# --- encontrar la posicion del 8 en ambas listas 
# primer lista
print(numeros.index(8))
# segunda lista 
print(nueva_lista.index(8))