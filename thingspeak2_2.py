Aquí te dejo el código mejorado con comentarios profesionales y claros, formato y estructura mejorada:

```python
# Importación de bibliotecas necesarias
import time
import random
import requests
import json

# Definición de claves para escritura y lectura en Thingspeak
KEY = "GZEN53T0T63XDDRJ"  # Poner aquí su Key de escritura
KEYREAD = "1283406"  # Poner aquí su key de lectura

try:
    while True:
        # Prueba 1: Escritura de datos a Thingsboard (hacerlo durante 90 segundos)
        # Generación de valores aleatorios para los campos
        value_1 = random.randint(-150, -50)
        value_2 = random.randint(-50, 50)
        value_3 = random.randint(50, 90)
        value_4 = random.randint(90, 150)
        value_5 = random.randint(150, 190)
        value_6 = random.randint(190, 290)

        # Creación de la lista con los valores
        lista = [value_1, value_2, value_3, value_4, value_5, value_6]

        # Verificación de que se han generado 6 valores
        if len(lista) == 6:
            # Envío de los datos a Thingspeak
            enviar = requests.get(
                f"https://api.thingspeak.com/update?api_key={KEY}&field1={lista[0]}&field2={lista[1]}"
                f"&field3={lista[2]}&field4={lista[3]}&field5={lista[4]}&field6={lista[5]}"
            )

            # Verificación del estatus de la solicitud
            if enviar.status_code == requests.codes.ok:
                if enviar.text != '0':
                    print("Datos enviados correctamente")
                else:
                    print("Tiempo de espera insuficiente (>15seg)")
            else:
                print(f"Error en el request: {enviar.status_code}")

        # Prueba 2: Lectura de datos desde Thingsboard
        recibir = requests.get(f"https://api.thingspeak.com/channels/{KEYREAD}/feeds.json")

        # Deserialización del JSON recibido
        data = recibir.json()

        # Imprime la información completa
        print("toda la info es : ")
        print(json.dumps(data, indent=2))

        # Prueba 3: Lectura de los valores de los campos
        feeds = data.get("feeds")
        if feeds:
            for feed in feeds[:3]:  # Mostrar solo los primeros 3 valores
                print("*************************************************")
                print(json.dumps(feed, indent=2))
                print(f"Variable1: {feed.get('field1')}")
                print(f"Variable2: {feed.get('field2')}")
                print(f"Variable3: {feed.get('field3')}")

        # Pausa durante 1 segundo
        time.sleep(1)
except Exception as e:
    print(f"Error crítico: {e}")
```

Espero que esto te sea útil. ¡Si tienes alguna pregunta o necesitas más ayuda, no dudes en preguntar!