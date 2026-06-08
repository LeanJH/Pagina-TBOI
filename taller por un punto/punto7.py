#par o impar
pares = 0
impares = 0

for i in range(10):
    numero = int(input(f"ingrese el número {i+1}: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
        
print(f"cantidad de pares: {pares}")
print(f"cantidad de impares: {impares}")
