# gestionar los empleados de una empresa 
empleados = {
    'juan' : {
        'salario' : 150,
        'departamento' : 'marketing'
    },
    'pedro' : {
        'salario' : 200,
        'departamento' : 'desarollo'
    },
    'carla' : {
        'salario' : 70,
        'departamento' : 'administración'
    }
}

# emplear ciclo while para que el usuario use el programa y seleccione la funión que el quiera 
while True:
    # mostrar opciones a usuario
    seleccion = input(('Selecciona una opción: \n1: Agregar nuevos empleados\n2: actualizar el salario de un empleado\n3: Mostrar lista completa de empleados\n4: calcular promedio salarial por departamento\nEscribe "fin" para cerrar el programa '))
    # salimos del programa
    if seleccion.lower() == 'fin':
        break
    # verificamos cuál función solicitó el usuario
    if int(seleccion) == 1:
        # ingresamos nuevo empleado
        nuevo_empleado = input('Ingresa el nombre del nuevo empleado: ')
        if nuevo_empleado in empleados:
            print(f'{nuevo_empleado.title()} ya está en el sistema')
            print('------------------------')
        else:
            empleados[nuevo_empleado] = {'salario' : 0, 'departamento' : ''}
    elif int(seleccion) == 2:
        # actualizar salario de empleado existente 
        actualizar_salario_emp = input('Ingresa el nombre del empleado a actualizar: ')
        if actualizar_salario_emp.lower() not in empleados:
            print(f'El empleado {actualizar_salario_emp.title()} no está en el sistema')
            print('---------------------')
        else:
            salario_actualizado = int(input('Ingresa el salario actualizado: '))
            empleados[actualizar_salario_emp.lower()]['salario'] = salario_actualizado
            print(empleados[actualizar_salario_emp.lower()])
            print('----------------------------')
    elif int(seleccion) == 3:
        # mostrar lista completa de empleados 
        for empleado,datos in empleados.items():
            print(empleado.title(), ':', datos)
    elif int(seleccion) == 4:
        # calcular el promedio salarial por departamento
        departamentos = {} # diccionario donde se almacenan los departamentos

        # Iterar sobre los empleados y agregar sus salarios al departamento correspondientez
        for empleado, datos in empleados.items():
            departamento = datos['departamento']
            salario = datos['salario']

            if departamento in departamentos:
                departamentos[departamento].append(salario)
            else:
                departamentos[departamento] = [salario]
        # calcular el promedio de cada departamento e imprimirlos 
        for departamento, salarios in departamentos.items():
            promedio = sum(salarios) / len(salarios)
            print(f'El promedio salarial para el departamento {departamento} es: {promedio}')
    else:
        print('No existe esta opción, favor de ingresar otra.')
        