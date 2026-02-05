```
#!/usr/bin/env python3

"""
Blink an LED connected to a Raspberry Pi's GPIO pin.

Author: Tonny
Date: 05/02/2026

This script initializes the GPIO, configures it for output,
and enters an infinite loop where it toggles the state of the LED.
"""

import RPi.GPIO as GPIO
import time
import signal

# --- Configuración GPIO ---
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pin configuration: 17 (BCM numbering) is used for the LED
# Define a constant for readability and maintainability
LED_PIN = 17

"""
Configure the GPIO pin as an output.
"""
GPIO.setup(LED_PIN, GPIO.OUT)


def cleanup_and_exit(signum, frame):
    """
    Function to be executed when a SIGINT or SIGTERM signal is received.

    Parameters:
        signum (int): The signal number that was received.
        frame (object): The current execution stack frame.

    Returns:
        None
    """
    print(f"\nReceived termination signal ({signum}). Cleaning up GPIO pins...")
    # Ensure the LED is turned off before cleanup
    GPIO.output(LED_PIN, GPIO.LOW)
    # Clean up all GPIO pins
    GPIO.cleanup()
    print("GPIO pins cleaned. Exiting program.")
    # Exit the script cleanly
    exit(0)


# Register signal handlers for SIGINT and SIGTERM signals
signal.signal(signal.SIGINT, cleanup_and_exit)  # For Ctrl+C
signal.signal(signal.SIGTERM, cleanup_and_exit)  # For 'systemctl stop'

print(f"Initializing LED blink on GPIO pin {LED_PIN}. The script can now be safely terminated.")

# Main loop: toggle the LED state every 0.5 seconds
while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.5)  # Pause for 0.5 seconds before switching states
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)  # Pause for another 0.5 seconds before repeating
```
