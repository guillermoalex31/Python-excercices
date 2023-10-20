# --- pedirle al usuario un número entero
num = int(input('Ingresa un número entero: '))

# --- bucle para imprimir la figura de * de uno hasta num 
for i in range(num+1):
    print('*'*i) 

# --- bucle para imprimir de num hasta 1
for i in range(num-1, 0, -1):
    print('*'*i)