import time
import psutil # Librería para ver el uso de hardware
import os

def stress_test(n):
    print(f"PID: {os.getpid()} - Iniciando cálculo en Python...")
    start_time = time.time()
    
    # Operación que estresa la ALU (Unidad Aritmético Lógica)
    count = 0
    for i in range(n):
        count += i
        
    end_time = time.time()
    print(f"Resultado: {count}")
    print(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos")

if __name__ == "__main__":
    # 10 millones de iteraciones
    stress_test(10_000_000)