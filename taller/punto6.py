#Descuento
total = 0
cantidad = int(input("¿Cuántos artículos desea comprar? "))
for i in range(cantidad):
    precio = float(input(f"Ingrese el precio del artículo {i+1}: "))
    total += precio
if cantidad < 10:
    print("no aplica descuento")
    total *= 1
else:
    cantidad > 10
    print("si aplica el descuento del 10%")
    total *= 0.90
print(f"El total de la factura es: ${total:.2f}")
