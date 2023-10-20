# pedir datos del usuario 
name = input('Ingresa tu nombre: ')
age = int(input('Ingresa tu edad: '))
average_grade = float(input('Ingresa tu promedio de calificaciones: '))

# ver si es elegible para la beca, tiene que tener entre 17 y 21 años y un promedio de 8 en adelante 
if (age >=17) and (age <= 21) and (average_grade >= 8):
    print('¡Felicidades!', name.title(), ',eres elegible para el programa de becas.')
else:
    print('No eres elegible para aplicar a alguna beca.')
