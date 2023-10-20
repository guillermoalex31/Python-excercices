# pedrile el nombre y sexo al usuario 
sexo = input('Introduce tu sexo (masculino/femenino) ')
name = input('¿Cuál es tu nombre? ')

# convertir el seño y nombre a minusculas 
name = name.lower() 
sexo = sexo.lower()

# asignación de grupos 
if sexo == 'femenino':
    if name >= 'e' and name <= 'm':
        print('Tu grupo es el A')
    else:
        print('Tu grupo es el B')
elif sexo == 'masculino':
    if name >= 'a' and name <= 'h' or name >= 'r' and name <= 'z':
        print('Tu grupo es el A')
    else: 
        print('Tu grupo es el B')
else:
    print('No ingresaste el sexo correcto, vuelve a intentarlo')