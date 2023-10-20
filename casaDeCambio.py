# definir variables
precio_euro = 1.2
comision = .10

# impimir la tasa de cambio de euro-dolar
print('Precio actual de Euro: ', precio_euro)

# peirle al usuario que ingrese la cantidad que quiere cambiar 
euros_usuario = float(input('Ingresa la cantidad de Euros que quieres cambiar: '))

# motrarle al usuario la tasa de cambio actual y devolverle el total de dolares 
print(euros_usuario, ' Euros, equivalen a: ', euros_usuario*precio_euro, ' USD')

# restarle el % de comsión de la casa de cambio 
print('Comision de la casa de cambio: 10%')

comision_total = comision*(precio_euro*euros_usuario)
print('Total: ', precio_euro*euros_usuario-comision_total, ' USD')