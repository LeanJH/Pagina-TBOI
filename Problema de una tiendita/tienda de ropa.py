#stoc en tienda de ropa nike en la que muestro como se tiene un inventario el cual al ejeutar me debe de dar las cantida de stock que queda del producto y si estos no suplen con la cantidad
#se debe de re ordenar y me entrega cuantos debo de pedir y en cuanto me sale mas el total a pagar por todo el pedido

productos = [
    {"id": 1, "nombre": "Camiseta hombre XL",   "stock_actual": 5,  "nivel_reorden": 10, "stock_objetivo": 30, "precio_unitario": 55000.0},
    {"id": 2, "nombre": "Gorra niño",      "stock_actual": 12, "nivel_reorden": 5,  "stock_objetivo": 20, "precio_unitario": 24000.5},
    {"id": 3, "nombre": "licra deportiva dama",   "stock_actual": 2,  "nivel_reorden": 5,  "stock_objetivo": 25, "precio_unitario": 60000.0},
    {"id": 4, "nombre": "Calcetines pack de 3", "stock_actual": 50, "nivel_reorden": 15, "stock_objetivo": 60, "precio_unitario": 15000.0},
    {"id": 5, "nombre": "bolso deportivo pequeño", "stock_actual": 10, "nivel_reorden":11, "stock_objetivo":11, "precio_unitario": 70000.0},
]

for i in productos :
    print(f"el producto {i['nombre']} tiene la cantida de {i['stock_actual']} en stock")

print("productos que necesitan reabastecimiento:")
total = 0

for p in productos:
    if p["stock_actual"] < p["nivel_reorden"]:
        cantidad_a_pedir = p["stock_objetivo"] - p["stock_actual"]
        costo = cantidad_a_pedir * p["precio_unitario"]
        total += costo
        print(f"{p['nombre']}: pedir {cantidad_a_pedir} unidades (costo: ${costo:.2f})")

print(f"costo total del pedido: ${total:.2f}")