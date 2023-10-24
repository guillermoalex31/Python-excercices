red_social = [("Juan", ["Maria", "Pedro","Luis"]), 
              ("Maria", ["Juan", "Pedro","Juan"]), 
              ("Pedro", ["Juan", "Maria"]), 
              ("Luis", ["Juan"])]

# Convertir a un set para eliminar duplicados y luego volver a convertirlo a una lista
sin_duplicados = []
for usuario, amigos in red_social:
    amigos_unicos =list(set(amigos))
    sin_duplicados.append((usuario, amigos_unicos))
# Imprimir la nueva lista sin duplicados
print(tuple(sin_duplicados))

# contar el número de amigos de cada usuario 
amigos_por_usuario = []
for usuario, amigos in sin_duplicados:
    amigos_por_usuario.append((usuario, len(amigos)))
amigos_por_usuario = tuple(amigos_por_usuario)
print(f'número de seguidores por usuario {amigos_por_usuario}')

# encontar al usuario con mas amigos
numero_amigos = [tupla[1] for tupla in amigos_por_usuario]

indice_con_mas_amigos = numero_amigos.index(max(numero_amigos))

print(f'El usuario con mas amigos es: {amigos_por_usuario[indice_con_mas_amigos][0]}')
