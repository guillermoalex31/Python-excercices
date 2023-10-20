# definir la contraseña del usuario 
contraseña = 'abc123'

# pedirle al usuario que ingrese la contraseña
contraseña_usuario = input('Ingresa la contraseña: ')

# validar la contraseña
if contraseña_usuario.lower() == contraseña:
    print('Bienvenido')
else:
    print('Contraseña incorrecta, vuelve a intentarlo')
    contraseña_usuario = input()
    if contraseña_usuario.lower() == contraseña:
       print('Bienvenido')
    else:
        print('Cuenta bloqueada por 24 hrs') 
