# base de datos con la información de los alumnos 
base_datos = []

# definir la cadena de caracteres con la información del alumno 
cadena = 'David Fernandez 123112A 43275 3 2.1 4.6 3.4'

# convertir la cadena de caracteres en una lista 
datos_alumno = cadena.split() #separa cada palabra del texto 

# introducir la lista en a base de datos de los alumnos 
base_datos.append(datos_alumno)

# recorrer la base de datos para sacar su DNI y la  nota media 
for alumno in base_datos:
    dni = alumno[2]
    # calcular la media de los alumnos 
    suma_notas = 0
    for i in range(5,len(alumno)):
        suma_notas += float(alumno[i])
    media = suma_notas / 3
    print(f'El alumno con DNI {dni} tiene una media de {media :.2f}')