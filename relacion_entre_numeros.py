# pedirle al usuario tres números diferentes 
num1 = int(input('Ingresa el primer número: '))
num2 = int(input('Ingresa el segundo número: '))
num3 = int(input('Ingrese el tercer número: '))

# indicar si alguno de los números es la suma de los otros dos 
if num2 + num3 == num1:
    print(num1, 'es resultado de la suma de', num2, '+', num3)
elif num1 + num3 == num2:
    print(num2, 'es el resultado de la suma de', num1, '+', num3)
elif num1 + num2 == num3:
    print(num3, 'es el resultado de la suma de', num1, '+', num2)
else:
    print('Ninguno de los números es el resultado de la suma de los anteriores.')