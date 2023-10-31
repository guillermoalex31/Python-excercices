jugadores = {
    'jugador1' : {
        'nombre' : 'pedro',
        'puntaje' : 53
    }
}

# pedirle al usuario que se registre su nombre y puntaje 
nombre_jugador = input('Ingresa tu nombre: ')
puntaje_jugador = int(input('Ingresa tu puntaje: '))

# añadir los datos al diccionario 
jugadores['jugador2'] = {'nombre' : nombre_jugador, 'puntaje' : puntaje_jugador}

# Inicializar variables para el puntaje mayor y la suma de puntajes
puntaje_mayor = 0
suma_puntajes = 0

# Iterar sobre los jugadores
for jugador, datos in jugadores.items():
    nombre = datos['nombre']
    puntaje = datos['puntaje']
    print(f'Jugador: {nombre.title()}\nPuntaje: {puntaje}')

    # Actualizar la suma de puntajes
    suma_puntajes += puntaje

    if puntaje > puntaje_mayor:
        puntaje_mayor = puntaje

# Calcular el promedio de puntaje
promedio_puntaje = suma_puntajes / len(jugadores)

# Imprimir todos los datos
print(f'El mayor puntaje es de {puntaje_mayor} puntos\nEl promedio de puntaje es de {promedio_puntaje}\nEl número de jugadores es de {len(jugadores)}')
