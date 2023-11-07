# crear funcion que valide un formulario de registro, nombre, correo electrónicom teléfono 
def validar_formulario(nombre, correo, telefono):
    while len(nombre) < 3:
        nombre = input('El nombre debe de tener una longitud mínima de 3 letras, por favor introduce un nombre válido: ')

    while '@' and '.' not in correo:
        correo = input('Ingresa un correo válido: ')

    while not (telefono.isdigit() and len(telefono) == 9):
        telefono = input('Ingresa un número de teléfono válido: ')

    print('Datos válidos')


nombre_usuario = input('Ingresa tu nombre: ')
correo_usuario = input('Ingresa tu correo electronico: ')
telefono_usuario = input('Ingresa tu número de teléfono: ')

validar_formulario(nombre_usuario, correo_usuario, telefono_usuario)
