#Pin correcto
pin_correcto= "4444"
pin = ""
while pin != pin_correcto:
    pin = input("ingresa tu pin: ")
    if pin != pin_correcto:
        print ("pin incorrecto, intenta otra vez.")
print ("acceso concedido")
               