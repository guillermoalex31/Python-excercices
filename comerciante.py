productos = [['producto1', 30, 3], ['producto2', 9.8, 1], ['producto3', 42.5, 0], ['producto4', 32.6, 0], ['producto5', 71.5, 7], ['producto6', 44, 2], ['producto7', 21.2, 0], ['producto8', 53.2, 0], ['producto9', 25.3, 4], ['producto10', 57.8, 0]]

# imprimir la cantidad total de ventas, ventas por producto y facturación total 
ventas = 0
facturacion = 0
for producto in range(len(productos)-1):
    print(f'Las ventas totales del {productos[producto][0]} son {productos[producto][2]}')
    ventas += productos[producto][2]
    if productos[producto][2] > 0:
        facturacion += productos[producto][2] * productos[producto][1]
print('------------------------------')
print(f'Ventas totales: {ventas}')
print('------------------------------')
print(f'Facturación: {facturacion}')
