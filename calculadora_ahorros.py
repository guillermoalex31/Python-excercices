# pedrile el nombre al usuario 
name = input('¿Cuál es tu nombre? ')
print('Bienvenido', name.title())

# pedirle las horas trabajadas en la semana y el dinero ganado por hora 
dinero = int(input('¿Cuánto ganas por hora? '))
tiempo = int(input('¿Cuántas horas trabajas a la semana? '))

# obtener el salario semanal lumtiplicando las dos variables 
salario_semanal =  tiempo * dinero

# calcular las ganancias anuales 
ganancias_anuales = salario_semanal * 52.1429

# imprimir as ganancias anuales del usuario 
print(name.title(), ' tiene unas ganancias anuales de:', ganancias_anuales, 'de MXN.')

# pedir gastos semanales 
gastos_semanales = int(input('¿Cuáles son tus gastos semanales? '))

# calcular los gastos anuales
gastos_anuales = gastos_semanales * 52.1429

# calcular los ahorros anuales 
ahorros = ganancias_anuales - gastos_anuales

# imprimir los resultados en pantalla 
print('Tus ahorros anuales son:', ahorros, 'de MXN.')
