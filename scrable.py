palabras = [['A',5], ['C',4], ['G',6], ['M', 9]]

# calcular los puntos que tiene la lista de palabras sumandolos todos 
resultado = 0
for i in range(len(palabras)): 
    resultado += palabras[i][1]
print(f'El puntaje de la lista es de {resultado}.')