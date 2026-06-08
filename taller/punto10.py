#lista de compra
productos = [{"nombre": "huevo", "precio": 200, "cantidad": 3},{"nombre": "1 kg azucar", "precio": 3500, "cantidad": 2},{"nombre": "pan", "precio": 2200, "cantidad": 2}]
print("factura de compra")
total = 0
for producto in productos:
    subtotal = producto["precio"] * producto["cantidad"]
    print(f"{producto['nombre']} x {producto['cantidad']} = ${subtotal}")
    total += subtotal
print(f"total: ${total}")