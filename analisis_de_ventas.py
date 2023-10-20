# Lista de ventas por cada día del mes
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110,
140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]

# Lista con los días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Inicializar una lista para almacenar las ventas por día de la semana
ventas_por_dia = [0] * 7

# Variable para llevar la cuenta del día de la semana actual
dia_actual = 0

# bucle para sumar las ventas correspondientes a cada día de la semana 
for venta in ventas:
    ventas_por_dia[dia_actual] += venta
    dia_actual += 1
    if dia_actual == 7:
        dia_actual = 0

for i,dia in enumerate(dias_semana):
    print(f'Total de ventas en {dia}: {ventas_por_dia[i]}')