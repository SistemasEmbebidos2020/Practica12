#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import signal # Importamos el módulo signal

# --- Configuración GPIO ---
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)

# --- Nuestro manejador de señales ---
# Esta función se ejecutará cuando se reciba SIGINT o SIGTERM
def cleanup_and_exit(signum, frame):
    print(f"\nSeñal de detención recibida (Señal: {signum}). Limpiando pines GPIO...")
    # Aquí va tu código de limpieza
    GPIO.output(led_pin, GPIO.LOW) # Opcional: nos aseguramos que el LED quede apagado
    GPIO.cleanup()
    print("Pines limpiados. Saliendo del programa.")
    # Salimos del script
    exit(0)

# --- Registrar los manejadores para las señales ---
# Le decimos a Python que llame a nuestra función 'cleanup_and_exit' cuando ocurran estas señales:
signal.signal(signal.SIGINT, cleanup_and_exit)  # Para Ctrl+C
signal.signal(signal.SIGTERM, cleanup_and_exit) # Para 'systemctl stop'

print(f"Iniciando parpadeo en el pin GPIO {led_pin}. El script ahora puede ser detenido de forma segura.")

# --- Bucle principal ---
# Ya no necesitamos el bloque try/except/finally
while True:
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(0.5)
