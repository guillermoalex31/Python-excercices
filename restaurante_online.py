# preguntaarle al usuario que tipo de haburguesa quiere 
hamburguesa = input('¿Qué tipo de haburguesa quieres? (clasica/vegana) ')

# enseñar los diferentes ingredientes de cada hamburguesa 
if hamburguesa.lower() == 'clasica':
    print('Los ingredientes extra son:\nQueso\nBacon\nHuevo')
    extra = input('Ingresa no, en el caso de no querer ninguno ')
    print('La haburguesa que pediste es', hamburguesa, '\nExtras:', extra.title())
elif hamburguesa.lower() == 'vegana':
    print('Los ingredientes extra son:\nTofu\nCebolla')
    extra = input('Ingresa no, en el caso de no querer ninguno ')
    print('La haburguesa que pediste es', hamburguesa, '\nExtras:', extra.title())
else:
    print('La hamburguesa que ingresaste no está diponible')
    