# Tomado de asistencia
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
num_alumnos = 5
for dia in dias:
    print(f"Registro de asistencia para el día {dia}")
    asistencias = []  
    for i in range(1, num_alumnos + 1):
        asistio = int(input(f"¿El alumno {i} asistió? (1=Sí, 0=No): "))
        asistencias.append(asistio)
    total_asistieron = sum(asistencias)
    print(f"En {dia} asistieron {total_asistieron} alumnos.")
