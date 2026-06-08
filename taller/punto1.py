#control de acceso
Pin_correcto= "131313"
intentos= 0
max_intentos=3

while intentos < max_intentos:
    pin=input(f"ingrese la contraseña:")
    if pin==Pin_correcto:
        print(f"Contraseña Correcta, Acceso permitido")
        break
    else:
        intentos+=1
        if intentos < max_intentos:
            print(f"contraseña incorrecta, quedan {max_intentos - intentos } intentos")
        else:
            print("has excedido el numero de intentos, Acceso denegado")
            