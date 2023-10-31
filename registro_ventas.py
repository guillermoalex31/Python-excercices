# registrar las ventas de cada producto y calcular las ventas totales del día 
productos = {
    'manzana' : 15,
    'plátano' : 10,
    'pera' : 16,
    'limon' : 20
}

# calcular las ventas diarias 
ventas_diarias = sum(productos.values())
print(f'Las ventas de hoy fueron: ${ventas_diarias}')