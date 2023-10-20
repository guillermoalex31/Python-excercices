# inicializar una lista con los datos de usuario y contraseña 
usuarios_y_contraseñas = [['maria71', 'maria123'], ['pedrox','p3dr0'], ['carlitox', 'c4rl05']]

# pedirle al usuario que ingrese usuario y contraseña 
usuario = input('Ingresa tu usuario: ')
contrasena = input('Ingresa tu contraseña: ')
datos_correctos = False

# validar si usuario y contraseña son correctas 
for user in usuarios_y_contraseñas:
    if usuario and contrasena in user:
        datos_correctos = True

# imprimir si es bienvenido o no 
if datos_correctos:
    print('Bienvenido')
else:
    print('Datos incorrectos, vuelve a intentarlo')