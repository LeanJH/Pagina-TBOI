#clasificando edades
while True:
    consulta = input("Ingrese la edad del cliente (o escriba FIN para terminar):")
    if consulta.lower() == "fin":
        print("Clasificacion Finalizada")
        break
    if consulta.isdigit():
        edad = int(consulta)
        if edad < 0:
            print("Edad no válida. Intente de nuevo.")
        elif edad < 18:
            print("Cliente clasificado como: Niño")
        elif edad < 60:
            print("Cliente clasificado como: Adulto")
        else:
            print("Cliente clasificado como: Adulto Mayor")
    else:
        print("entrada no válida. escriba una edad numérica o FIN.")