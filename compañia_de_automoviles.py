# definir los precios de los autos y comision aplicada 
serie_1 = 20000 * .03
plus = 35000 * .05
todoterreno = 60000 * .07

# Pedirle al usuario que ingrese el número de autos vendidos de cada tipo 
ventas_Serie_1 = int(input('Ingresa el número de ventas del serie 1: '))
ventas_plus = int(input('Ingresa el número de ventas del serie plus: '))
ventas_todoterreno = int(input('Ingresa el número de ventas del todo terreno: '))

# devolverle al usuario el total de sus comisiones y desglosar cada una 
print('----------------------------------------')
print('Comisiones de venta de serie 1: ', serie_1*ventas_Serie_1)
print('Comisiones de venta de serie plus: ', plus*ventas_plus)
print('Comisiones de venta de todoterreno: ', todoterreno*ventas_todoterreno)
print('----------------------------------------')
print('Total: ', serie_1*ventas_Serie_1 + plus*ventas_plus + todoterreno*ventas_todoterreno)

