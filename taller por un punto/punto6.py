#promedio de notas
notas = []
cantidad = int(input("¿Cuántas notas quieres ingresar?: "))

for i in range(cantidad):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)
print(f"el promedio es: {promedio:.2f}")

if promedio >= 4.5:
    print("Resultado: excelente")
elif promedio >= 3.0 and promedio < 4.5:
    print("Resultado: aprobado")
else:
    print("Resultado: reprobado")