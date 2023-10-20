# pedir datos del usuario 
edad = int(input('¿Qué edad tienes? '))
ingresos = int(input('Ingresa tus ingresos mensuales: '))

# calcular el porcentaje de impustos que debe de pagar el usuario 
if ingresos < 1000 and edad >= 18:
    print('Aún no debes de pagar impuestos!')
elif ingresos < 15000 and edad >= 18:
    impuestos = ingresos * .05
    print('Tienes que pagar', impuestos)
elif ingresos >=15000 and ingresos < 25000 and edad >= 18:
    impuestos = ingresos * .15
    print('Tienes que pagar', impuestos)
elif ingresos>=25000 and ingresos < 35000 and edad >= 18:
    impuestos = ingresos * .2
    print('Tienes que pagar', impuestos)
elif ingresos >= 35000 and ingresos < 60000 and edad >= 18:
    impuestos = ingresos * .3
    print('Tienes que pagar', impuestos)
else:
    impuestos = ingresos * .45
    print('Tienes que pagar', impuestos)
