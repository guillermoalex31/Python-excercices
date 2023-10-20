# pedirle al usuario 4 números diferentes
num1 = int(input('Ingresa el primer número: '))
num2 = int(input('Ingresa el segundo número: '))
num3 = int(input('Ingresa el tercer número: '))
num4 = int(input('Ingresa el último número '))

# comprobar cuál es el mayor de los 4 
if num1 > num2 and num1 > num3 and num1 > num4:
    print(num1, 'es el número mayor.')
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(num2, 'es el número mas grande.')
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(num3, 'es el número mas grande.')
else: 
    print(num4, 'es el número mas grande.')