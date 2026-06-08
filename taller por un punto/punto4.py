#encuesta 
print("Encuesta de satisfacción (responde con'bueno','regular'o'malo')")

respuestas = []
for i in range(5):
    r = input(f"Cliente {i+1},¿cómo califica el servicio?:").lower()
    respuestas.append(r)

print("encuesta finalizada, las respuestas fueron:", respuestas)