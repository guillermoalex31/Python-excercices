lista_libros = [('El aleph', 'Jorge Luis Borges'), ('Cien años de soledad', 'Garbriel Garcia Márquez'), ('La ciudad y los perros','Mario Vargas Llosa')] 

# separar libro y autor
libros_y_apellidos = [] 
for libro, autor in lista_libros:
    apellido = autor.split()[-1]
    libros_y_apellidos.append((libro, apellido))
print(libros_y_apellidos)