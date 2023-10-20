# pedirle al usuario que agregue el número a elevar 
num  = int(input('Ingresa el número que quieres elevar: '))

# pedrile al usuario que ingrese la potencia 
potencia = int(input('Ingresa la potencia: '))

# elevar a la potencia num 
resultado = num**potencia

# comprobar si es par o impar e imprimir el resultado 
if resultado % 2 == 0:
    print(num, 'elevado a la potencia de', potencia, 'da como resultado:', resultado, 'y es par.')
else:
     print(num, 'elevado a la potencia de', potencia, 'da como resultado:', resultado, 'y es impar.')
     