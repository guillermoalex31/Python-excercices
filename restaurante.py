# definir los precios del menú 
ensalada_mixta = 12
sopa_pescado = 10
dorada_al_horno = 18
arroz_curry = 14
lasaña_de_carne = 15
brownie_chocolate = 8
helado = 6
refrescos = 5.5
cafe = 3.5

# pedirle al usuario que ingrese la cantidad de platillos 
print('Ingrese la cantidad de cada alimento consumido')
cantidad_ensalada = int(input('Ensalada mixta: '))
cantidad_sopa = int(input('Sopa de pescado: '))
cantidad_dorada = int(input('Dorada al horno: '))
cantidad_arroz = int(input('Arroz curry: '))
cantidad_lasaña = int(input('Lasaña de carne: '))
cantidad_brownie = int(input('Brownie de chocolate: '))
cantidad_helado = int(input('Helado: '))
cantidad_refrescos = int(input('Refrescos: '))
cantidad_cafe = int(input('Café: '))

# calcular la cuenta 
total = cantidad_ensalada*ensalada_mixta + sopa_pescado*cantidad_sopa + dorada_al_horno*cantidad_dorada + arroz_curry*cantidad_arroz + lasaña_de_carne*cantidad_lasaña + brownie_chocolate*cantidad_brownie + helado*cantidad_helado + refrescos*cantidad_refrescos + cafe*cantidad_cafe

print('-----------------------------------')
print('El total de la cuenta es ', total, 'Euros')