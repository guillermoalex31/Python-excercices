# --- definir la contraseña 
contraseña = 'abc123'
usuario_contraseña = ''

# --- crear bucle pidiendole la contraseña al usuario hasta que la adivine 
while usuario_contraseña != contraseña:
    usuario_contraseña = input('Introduce la contraseña: ')
    if usuario_contraseña != contraseña:
        print('Contraeña incorrecta, intentalo de nuevo')

# darle la bienvenida al usuario
print('Bienvenido')