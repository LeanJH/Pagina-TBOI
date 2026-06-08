#Edades
print("Encuesta de edades")
edades = []
edad = int(input("Ingrese una edad (-1 para terminar): "))
while edad != -1:
    if 0 <= edad <= 120:
        edades.append(edad)
    else:
        print("Edad inválida. Debe estar entre 0 y 120.")
    edad = int(input("Ingrese una edad (-1 para terminar): "))
print("Cantidad de edades registradas:", len(edades))
if len(edades) > 0:
    print("Edad mínima:", min(edades))
    print("Edad máxima:", max(edades))
else:
    print("No se ingresaron edades válidas.")