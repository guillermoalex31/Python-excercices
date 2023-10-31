asistencias = dict()

# registro de asistencias de estudiantes 
asistencias['mario'] = ['2023-03-06', '2023-03-10', '2023-03-13']
asistencias['paola'] = ['2023-03-03', '2023-03-14', '2023-03-13']

# agregar nuevas fechas de asistencia 
asistencias['mario'].append('2023-04-19')
asistencias['paola'].append('2023-03-20')

# mostrar lista de estudiantes y fechas en las que asistieron 
for estudiante in asistencias:
    print(f'Asisencias de {estudiante.title()}:')
    for dias in asistencias[estudiante]:
        print(dias)
