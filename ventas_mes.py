# importar modulos
import numpy as np

# Datos de ventas de la tienda / input
ventas = np.array([
    ['2022-01-01', 100, 'ropa'],
    ['2022-01-02', 200, 'alimentos'],
    ['2022-01-03', 150, 'ropa'],
    ['2022-02-01', 120, 'alimentos'],
    ['2022-02-02', 180, 'electrónicos'],
    ['2022-02-03', 200, 'alimentos'],
    ['2022-03-01', 90, 'ropa'],
    ['2022-03-02', 110, 'electrónicos'],
    ['2022-03-03', 100, 'alimentos']
])

#extraer las fechas 
fechas = np.array([venta[0] for venta in ventas])

#extraer los meses de las fechas 
meses = np.array([int(fecha[5:7]) for fecha in fechas])

#sumar los montos de venta por mes
montos_mes = np.zeros(12)
for mes in range(1,13):
    ventas_mes = ventas[meses == mes]
    montos_mes[mes-1] = np.sum(ventas_mes[:,1].astype(int))

print(f'Monto total de ventas por mes: {montos_mes}')
