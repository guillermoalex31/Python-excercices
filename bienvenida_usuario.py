# preguntarle el usuario por pantalla 
usuario = input('¿Cuál es tu usuario? ')

# validar si el usuario es invitado o tiene cuenta y saludarlo 
if usuario.lower() == 'alejandro' or usuario.lower() == 'naomi' or usuario.lower() == 'sergio':
    print('Bienvenido', usuario.title())
else:
    print('Ingresaste como invitado, bienvenido', usuario.title())
