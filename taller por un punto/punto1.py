# Lista de stocks
inventario = {"frutas": 10, "pan": 4, "leche": 3}

for producto, cantidad in inventario.items():
    if cantidad < 5:
        print(f"{producto} está por acabarse, pedir más al proveedor.")
    else:
        print(f"{producto} tiene suficiente stock ({cantidad} unidades).")