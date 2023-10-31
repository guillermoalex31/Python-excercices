# analizar los votos obtenidos de un candidato en una elección 
candidatos = {
    'güero' : [12, 23, 32],
    'luci' : [11, 23, 9],
    'lupita' : [13, 23, 2]
}

while True:
    seleccion = input('Opciones: \n1: registrar nuevos votos\n2: Mostrar candidatos y votos\n3: encontrar candidato ganador\n4: calcular promedio de votos de cada candidato\n escribe "fin" para abandonar programa ')
    if seleccion.lower() == 'fin':
        break
    elif int(seleccion) == 1:
    # registrar nuevos votos 
        candidato = input('Ingresa el nombre del candidato: ')
        if candidato not in candidatos:
            print('El candidato no se encuentra en la base de datos')
        else: 
            votos = int(input('Ingresa los votos extras: '))
            candidatos[candidato.lower()].append(votos)
    elif int(seleccion) == 2:
        # mostrar los candidatos y votos}
        for candidato, votos in candidatos.items():
            print(candidato.title(), ':', sum(votos))
    elif int(seleccion) == 3:
        # Encontrar candidato ganador 
        max_votos = 0
        ganador = ""

        for candidato, votos in candidatos.items():
            total_votos = sum(votos)
        
            if total_votos > max_votos:
                max_votos = total_votos
                ganador = candidato

        print(f'El candidato ganador es: {ganador.title()} con un total de {max_votos} votos.')
    elif int(seleccion) == 4:
        # Mostrar candidatos y porcentaje de votos
        total_votos = sum(sum(votos) for votos in candidatos.values())

        for candidato, votos in candidatos.items():
            porcentaje = (sum(votos) / total_votos) * 100
            print(f'{candidato.title()}: {porcentaje:.2f}%')
    else:
        print('No existe esta opción, favor de ingresar otra.')
