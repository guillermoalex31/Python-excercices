# PEDIR INGRESAR LOS TIEMPOS DE LAS DEPORTISTAS 
tiempo_hanah = input('Ingresa el tiempo de Hannah en formato minutos, segundos, centésimas: ')
tiempo_jackie = input('Ingresa el tiempo de Jackie en formato minutos, segundos, centésimas: ')
tiempo_kimberly = input('Ingresa el tiempo de Kimberly en formato minutos, segundos, centésimas: ')

#separamos el tiempo de las deportistas  
minutos_hannah, segundos_hannah, centesimas_hannah = tiempo_hanah.split(' ')  #nos divide lo que esté dentro de los paréntesis 
minutos_jackie, segundos_jackie, centesimas_jackie = tiempo_jackie.split(' ')
minutos_kimberly, segundos_kimberly, centecimas_kimberly = tiempo_kimberly.split(' ')

#convertir el tiempo a segundos 
total_hannah = float(minutos_hannah) * 60 + float(segundos_hannah) + float(centesimas_hannah) * 0.01
total_jackie = float(minutos_jackie) * 60 + float(segundos_jackie) + float(centesimas_jackie) * 0.01
total_kimberly = float(minutos_kimberly) * 60 + float(segundos_kimberly) + float(centecimas_kimberly) * 0.01

# sacar la velocidad de los deportistas v=d/t e imprimirla
print('La velocidad de Hannah es de ',  100 / total_hannah, 'm/s')
print('La velocidad de Jackie es de ', 100  / total_jackie, 'm/s')
print('La velocidad de Kimberly es de ', 100 / total_kimberly, 'm/s')
