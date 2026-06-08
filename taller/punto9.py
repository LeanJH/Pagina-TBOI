#control de inventario
while True:
    unidades = int(input("Ingrese la cantidad en inventario del producto (0 o -1 para finalizar):"))
    if unidades == -1:
        print("Finalizo la revisión de inventario")
        break
    if unidades == 0:
        print("Cuidado:Un producto se quedó sin stock.")
        break
    else:
        print("Inventario revisado, quedan", unidades, "unidades.")