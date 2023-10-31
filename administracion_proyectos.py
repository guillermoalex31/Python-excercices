# debnemos administrar las tareas de cada equipo con el nombre de tarea, descripción y encargado
tareas = {}

# asiganmos tareas a cada equipo 
tareas['limpiar cocina'] = {'descripcion' : 'limpiar muy bien todos los utencilios de la csina', 'responsable' : 'john'}
tareas['limpiar mesas'] = {'descripcion' : 'limpiar las mesas despues de que los clientes terminen de comer', 'responsable' : 'juan'}

# reemplazar responsable de una tarea 
tareas['limpiar cocina']['responsable'] = 'maría'
# actualizar descripcion de tarea 
tareas['limpiar cocina']['descripcion'] = 'limpiar muy bien todos los utencilios de la cosina'

# mostrar lista completa de tareas y responsables 
for tarea, tarea_info in tareas.items():
    descripcion = tarea_info['descripcion']
    encargado = tarea_info['responsable']
    print(f'Tarea: {tarea.title()}\nDescripoción: {descripcion}\nResponsable: {encargado.title()}')
    print('-------------------------------------------------------')
