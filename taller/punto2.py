#Caja registradora
total = 0        
conteo = 0       
venta = float(input("Ingrese el monto de la venta (0 para finalizar): "))
while venta != 0:
    if venta < 0:
        print("Monto inválido. Debe ser >= 0.")
    else:
        total += venta   
        conteo += 1      
    venta = float(input("Ingrese el monto de la venta (0 para terminar): "))
if conteo == 0:
    print("No se registraron ventas.")
else:
    print("------ Resumen ------")
    print("Ventas registradas:", conteo)
    print("Total en ventas:", total)