# pedir al usuario que ingrese la medida de los tres lados del triángulo 
l1 = float(input('Ingresa la medida de un lado del trángulo: '))
l2 =  float(input('Ingresa la medida del segundo lado del triángulo: '))
l3 = float(input('Ingresa la medida del tercer lado del triángulo: '))

# comparar que uno de los lados sea mas grande que la suma de los dos anteriores 
if l2 + l3 > l1:
    print('Es posible hacer la base')
elif l1 + l3 > l2:
    print('Es posible hacer la base')
elif l1 + l2 > l3:
    print('Es posible hacer la base')
else:
    print('No es posible hacer la base')