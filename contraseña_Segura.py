# pedrile al usuario que ingrese una contraseña 
contraseña = input('Ingresa una contraseña segura con al menos una vocal minúscula y dos caraacteres especiales: ')

# comprobar si la contraseña es segura 
if 'a' in contraseña or 'e' in contraseña or 'i' in contraseña or 'o' in contraseña or 'u' in contraseña:
    if '*' and '#' in contraseña:
        print('Tu contraseña es segura')
    else:
        print('Tu contraseña debe de tener caracteres especiales (*,#)')
else:
    print('Tu contrasea debe de tener vocales minúsculas')
