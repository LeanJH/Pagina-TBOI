public class HardwareTest {
    public static void main(String[] args) {
        long n = 10_000_000;
        System.out.println("PID: " + ProcessHandle.current().pid() + " - Iniciando cálculo en Java...");
        
        long startTime = System.currentTimeMillis();
        
        // El compilador JIT de Java puede optimizar esto directamente en registros de CPU
        long count = 0;
        for (long i = 0; i < n; i++) {
            count += i;
        }
        
        long endTime = System.currentTimeMillis();
        System.out.println("Resultado: " + count);
        System.out.println("Tiempo de ejecución: " + (endTime - startTime) / 1000.0 + " segundos");
    }
}