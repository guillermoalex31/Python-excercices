texto_usuario = input('Introduce el texto a cifrar: ')  # Texto que se va a cifrar
alfabeto = "abcdefghijklmnopqrstuvwxyz"  # Alfabeto utilizado para el cifrado
alfabeto_upper = alfabeto.upper() # Alfabeto utilizado para el cifrado mayúsculas
mensaje_cifrado = ""  # Variable para almacenar el mensaje cifrado
letra = '' # Variable para almacenar cada letra del cifrado

# Bucle para recorrer cada letra del texto
for char in texto_usuario:
    # comproba si se encuentra en el alfabeto minpusculas 
    if char in alfabeto:
        # Encontrar la posición de la letra en el alfabeto
        for i in range(len(alfabeto)):
            if char == alfabeto[i]:
                char_id = i  # Índice original de la letra en el alfabeto

                new_id = char_id + 13  # Nuevo índice de la letra cifrada
                if new_id >= 26:  # Si el nuevo índice es mayor o igual a 26
                    new_id -= 26  # Restar 26 para asegurarse de que esté dentro del rango del alfabeto

                letra = alfabeto[new_id]  # Obtener la letra cifrada correspondiente al nuevo índice
        mensaje_cifrado += letra  # Agregar la letra cifrada al mensaje cifrado
    elif char in alfabeto_upper:
         # Encontrar la posición de la letra en el alfabeto
        for i in range(len(alfabeto_upper)):
            if char == alfabeto_upper[i]:
                char_id = i  # Índice original de la letra en el alfabeto

                new_id = char_id + 13  # Nuevo índice de la letra cifrada
                if new_id >= 26:  # Si el nuevo índice es mayor o igual a 26
                    new_id -= 26  # Restar 26 para asegurarse de que esté dentro del rango del alfabeto

                letra = alfabeto_upper[new_id]  # Obtener la letra cifrada correspondiente al nuevo índice
        mensaje_cifrado += letra  # Agregar la letra cifrada al mensaje cifrado
    else:
        mensaje_cifrado = mensaje_cifrado + char

print(mensaje_cifrado)  # Imprimir el mensaje cifrado