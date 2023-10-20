# pedir al usuario que introdusca un precio 
price = float(input('Ingresa el preciode BTC: '))

# mandar ensaje de compra, venta o hold 
if price < 100:
    print('Buy the dip')
elif price > 100 and price < 150:
    print('Hold')
else:
    print('Sell!!')