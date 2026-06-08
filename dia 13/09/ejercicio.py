#identificar positivos
def contar_positivos(lista):
    positivos = 0
    for numero in lista:
        if numero > 0:       
            positivos = positivos + 1
    return positivos

mis_numeros = [-1, 0, 3, 5, -2]
print("Total de positivos:", contar_positivos(mis_numeros))
