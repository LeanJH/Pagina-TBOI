#cajero automatico punto3
monto = int(input("Ingrese el monto a retirar: "))

if monto % 10000 == 0 and monto > 0:
    print(f"Retiro exitoso: ${monto}")
else:
    print("Monto inválido. Solo se permiten múltiplos de $10.000")