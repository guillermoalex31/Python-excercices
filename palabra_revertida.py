# --- pedrile al usuario una palabra
palabra = input('Ingresa una palabra: ')

# --- bucle para imprimir una a una cada letra de la palabra en orden invertido
for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])
