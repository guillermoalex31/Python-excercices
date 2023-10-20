numeros = [7, 43, 245, 76, 8, 53, 24, 5, 6, 7, 82, 2, 34, 65, 21, 63]
primos = []

# verificar si algún número dentro de la lista de números es primo 
for numero in numeros: 
    if numero > 1:
        es_primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(numero)

print(f'Los números primos de la lista son {primos}')

print(f'Total de números primos encontrados {len(primos)}.')

print(f'Suma de los números primos encontrados {sum(primos)}.')
