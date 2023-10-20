palabras = ['palo', 'perro', 'coco', 'gato', 'hola']
letras_prohibidas = ['x', 't', 'p']
palabras_aceptadas = []

# filtar las letras en una nueva lista que no contengan las letras prohibidas 
for palabra in palabras:
    letra_prohibida = False
    for letra in palabra:
        if letra in letras_prohibidas:
            letra_prohibida = True
            continue
    if not letra_prohibida:
        palabras_aceptadas.append(palabra)
print(palabras_aceptadas)
