#Buca de productos en inventario
inventario=("shampoo","jabon","escoba","trapera","pasta de dientes")
print("Busqueda de Productos(escriba salir para finalizar busqueda)")
while True:
 producto=input("introduzca el nombre del producto para saber si esta en el inventario:").lower()
 if producto=="salir":
     print("Busqueda Terminada")
     break
 disponible=False
 for item in inventario :
    if item==producto:
        disponible=True
    break
 if disponible:
     print(f"El producto '{producto}' está disponible en el inventario.")
 else:
    print(f"El producto '{producto}' NO se encuentra en el inventario.")