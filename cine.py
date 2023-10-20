# import modules
import numpy as np

# array con datos de peliculas
peliculas = np.array([    
    ['Peli 1', 'Comedia', 120, 1990, 8.5],
    ['Peli 2', 'Acción', 110, 2005, 7.8],
    ['Peli 3', 'Drama', 95, 2010, 6.9],
    ['Peli 4', 'Comedia', 100, 1985, 7.5],
    ['Peli 5', 'Acción', 130, 2015, 8.1],
    ['Peli 6', 'Drama', 115, 2000, 6.7],
    ['Peli 7', 'Comedia', 90, 1995, 8.2],
    ['Peli 8', 'Acción', 105, 2010, 7.4],
    ['Peli 9', 'Drama', 125, 1980, 6.8],
    ['Peli 10', 'Comedia', 95, 2000, 8.0]
])

#contar las repeticiones de cada genero 
generos, conteo = np.unique(peliculas[:,1], return_counts=True)

#ordemamos los conteos de menor a mayor 
conteos_dec = np.argsort(conteo) [::-1]

#extraer genero mas popular 
genero_popular = generos[conteos_dec[0]]
print(f'el genero mas popular es {genero_popular}')

#agrupar perlículas por decada 
decadas = np.unique(peliculas[:,3].astype(int) // 10 * 10)

conteos_decadas = []
for decada in decadas:
    conteo = np.count_nonzero((peliculas[:,3].astype(int) >= decada) & (peliculas[:,3].astype(int) < decada + 10))
    conteos_decadas.append(conteo)
    print(f'en la decada de {decada} se produjeron {conteo} películas')

#---duarcion promedio de cada genero 
todos_generos = peliculas[:,1]
duracion = peliculas[:,2]
duracion_media = np.zeros(len(generos))
for i in range(len(generos)):
    duracion_media[i] = np.mean(duracion[todos_generos == generos[i]].astype(float))
    print(f'la duracion media de las peliculas de {generos[i]} es de {duracion_media[i]:.2f} minutos')
