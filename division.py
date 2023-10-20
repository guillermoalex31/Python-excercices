# pedirle al usuario los dos números a dividir 
num1 = int(input('Ingresa el número que quieres dividir: '))
num2 = int(input('¿Entre cuanto lo quieres dividir? '))

# comprobar que el divisor no sea cero y si está bien, hacer la división 
if num2 == 0:
    num2 = int(input('No se puede dividir entre cero, vuelve a ingresar el divisor: '))

print('El resulado es ', num1/num2)
    