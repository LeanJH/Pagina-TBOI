#dias lluviosos
dias_lluviosos = 0
mes = int(input("¿Cuántos días tiene el mes a registrar? "))
for dia in range(1, mes + 1):
    reporte = input(f"¿Llovió el día {dia}? (s/n): ").lower()
    if reporte == "s":
        dias_lluviosos += 1
print(f"El total de días lluviosos en el mes fue: {dias_lluviosos}")