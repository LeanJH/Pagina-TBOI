#caja de minimercado
print("Bienvenido al Supermercado")

cliente = input("Ingrese el nombre del cliente: ").strip()   #pedimos el nombre del cliente

cantidad = int(input("¿Cuántos productos va a registrar? "))   #preguntamos cuántos productos comprará

total = 0.0  #acumulador del valor total de la compra

for i in range(1, cantidad + 1):    #ciclo para registrar los precios de cada producto
    precio = float(input(f"Ingrese el precio del producto {i}: "))  
    total += precio              #sumamos el precio al total


print(f"El total de la compra de {cliente} es: ${total:.2f}")    #mostramos el total de la compra


if total >= 65000:                                #condicional para que sea posible el descuento
    descuento = total * 0.10
    total -= descuento
    print(f"Se aplicó un 10% de descuento (${descuento:.2f}).")
    print(f"Total a pagar con descuento: ${total:.2f}")
else:
    print("No aplica descuento. Total a pagar es igual al valor de la compra.")
