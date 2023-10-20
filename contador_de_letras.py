# --- pedirle al usuario ingresar un texto y una letra 
frase = input('Ingresa una frase: ')
letra = input('Ingresa una letra: ')
contador = 0

# --- bucle para comprobar cuantas veces sale la letra en el texto 
for caracter in frase:
    if letra == caracter:
        contador += 1

# mostrar en pantalla el número de veces que aparece la letra en la frase 
print(f'La letra {letra.title()} aparece {contador} veces en la frase.')