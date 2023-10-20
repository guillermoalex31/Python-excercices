estudiantes = ['Juan', 'María', 'Pedro']

database = []

# pedirle al auaurio que ingrese las calificiones de los estudientes
for estudiante in estudiantes:
    # crear una lista interna donde se vayan guardando todos las calificaciones de cada alumno 
    notas = []
    print(f'ingresa las notas de {estudiante}')
    deberes = float(input('Notas de deberes: '))
    notas.append(deberes)
    examenes = float(input('Notas de examenes: '))
    notas.append(examenes)
    proyectos = float(input('Notas de proyectos: '))
    notas.append(proyectos)
    database.append([estudiante, notas])

# sacar promedio de estudiantes y del salón 
notas_salon = 0
for data in database:
    # extraemos los datos de la sublista 
    nombre = data[0]
    notas = data[1]
    # sacamos el promedio de casda estudiante 
    media = sum(notas   ) / len(notas)
    # imprimimos el promedio de cada estudiante
    print(f'La nota media de {nombre} es {media : .2f}')
    # guardamos las notas medias de cada estudiante en una variable para sacar el promedio
    notas_salon += media 
# calculamos e imprimimos la media del salón 
print(f'La media de todo el salón es {notas_salon  / len(database) : .2f}')
