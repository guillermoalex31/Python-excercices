import numpy as np

# Crear un array con los datos
datos = np.array([['2022-01-01', 'Componente 1', 'Lote A', 80],
                  ['2022-01-15', 'Componente 1', 'Lote B', 90],
                  ['2022-02-01', 'Componente 2', 'Lote C', 85],
                  ['2022-02-15', 'Componente 2', 'Lote D', 95],
                  ['2022-03-01', 'Componente 1', 'Lote E', 75],
                  ['2022-03-15', 'Componente 2', 'Lote F', 90]])

#identificar el componente con la puntuación mas alta 
tipos_componente = datos[:,1]
tipos_unicos = np.unique(tipos_componente)
calidad = datos[:,3].astype(float)

i = 0
promedios = np.zeros(len(tipos_unicos))
for tipo in tipos_unicos:
    promedios[i] = np.mean(calidad[tipos_componente == tipo])
    i += 1
indice_macimo = np.argmax(promedios)
tipo_mejor = tipos_unicos[indice_macimo]

print(f'el tipo de componente con la puntuacion mas alte es {tipo_mejor}')

# cuantos componenetes se produjeron cada mes 
fechas = datos[:,0]
meses, counts = np.unique([fecha[0:7]for fecha in fechas], return_counts=True) 

for i in range(len(meses)):
    print(f'mes: {meses[i]}. Cantidad producida: {counts[i]}')

#calidad promedio de cada componente 
promedio_por_tipo = np.zeros(len(tipos_unicos))
for i in range(len(tipos_unicos)):
    promedio_por_tipo [i]=  np.mean(calidad[tipos_componente == tipos_unicos[i]]) 
    print(f'la puntuacion de calidad promedio para el {tipos_unicos[i]} es {promedio_por_tipo[i]:.2f}')
