#crear un array con las calificaciones de los estudiantes 
import numpy as np 

#calificaciones de estudiantes
calificaciones = np.array([
    [9, 8, 10, 8],
    [10, 8, 9, 7],
    [9, 7, 8, 9],
    [9, 8, 10 ,9]
])

#calcular nota final de cada estudiante 
examen1 = calificaciones[:,0]
examen2 = calificaciones[:,1]
trabajo_final = calificaciones[:,2]
participacion = calificaciones[:,3]
nota_final = examen1 * .3 + examen2 * .3 + trabajo_final * .3 + participacion * .1

#imprimir las notas finales de cada estudiante 
for i in range(len(nota_final)):
    print(f'la nota final del estudiante {i+1} es {nota_final[i]}') 