# pedirle al usuario que ingrese los 8 dígitos de su tarjeta 
tarjeta = input('Ingresa los 8 dígitos de tu tarjeta bancaria: ')

# averiguar la longitud de la tarjeta 
longitud = len(tarjeta)

# imprimir solo los últimos digitos y los demas en *
print('*' * (longitud-4) + tarjeta[longitud-4:longitud])
