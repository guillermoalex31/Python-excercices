# crear una lista de frutas 
frutas = ['manzana', 'plátano', 'cereza', 'pera', 'higo', 'frambueza', 'fresa']

# imprimir la longitud de la lista 
print(len(frutas))

# imprimir la tercera fruta 
print(frutas[2])

# cambiar la fruta número 2 por mora
frutas[1] = 'mora'

# añadir mango al final de la lista 
frutas.append('mango')

# añadir uva al inicio de la lista
frutas.insert(0, 'uva')

# usar un bucle para imprimir casa fruta en consola 
for fruta in frutas:
    print(fruta)

# eliminar la última fruta y almacenarla en una variable 
fruta_eliminada = frutas.pop()

# imprimir la longitud de cada nombre de la fruta 
for i in range(len(frutas) -1):
    print(len(frutas[i]))

# bucle que solo imprima las frutas que tengan mas de 5 caracteres
for i in range(len(frutas) -1):
    if len(frutas[i]) >= 5:
        print(frutas[i])

# borrar cereza de la lista
frutas.remove('cereza')

# vaciar toda la lista 
frutas.clear()
