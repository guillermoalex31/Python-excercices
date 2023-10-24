base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria","maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", "555-9012")]

base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]), ("Luis", "Calle 789", ["Libro4"])] 

# unir ambas bases de datos pero solo con usuarios que se repiten en ambas bases de datos 
base_datos = []
for i in range(len(base_datos2)):
    if base_datos2[i][0] in base_datos1[i]:
        base_datos.append((base_datos2[i] + base_datos1[i][1::]))
print(base_datos)
