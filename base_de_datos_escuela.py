notas_estudiantes = [['Juan',9.5,9.3,8], ['Memo',9.8,9.3,8.9], ['Jess',8.4,9.2,8.7],['Alex',7.7,8.3,8],['Martín',9,8.6,8],['Luci',9,10,8],['Marcos',9,9,8],['Alexa',7.7,9,8]]
medias_estudientes = []

# calcular la nota media de cada estudiante 
for estudiante in notas_estudiantes:
   promedio = sum(estudiante[1:])/(len(estudiante)-1) 
   medias_estudientes.append(promedio)
print(medias_estudientes)

# calcular promedio de la clase
print(f'El promedio de la clase es de {sum(medias_estudientes) / len(medias_estudientes) -1}')
