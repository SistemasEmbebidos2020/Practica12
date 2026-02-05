# 💻 Proyecto Raspberry Pi: Control de LED con Blink y Sensores
==========================

## Descripción del proyecto

Este proyecto consiste en la creación de un script para controlar el estado de un LED conectado a un Raspberry Pi mediante pines GPIO. Además, se integran sensores para leer temperaturas y enviar los datos a plataformas de IoT como Thingspeak y Ubidots.

## Hardware requerido

* 1 x Raspberry Pi (versión 3 o superior)
* 1 x Led RGB
* 1 x Sensor de temperatura DS18B20
* Conectores para conectar el LED y el sensor al GPIO del Raspberry Pi

## Software y librerías

* Python 3.x
* RPi.GPIO (librería para interactuar con pines GPIO)
* Requests (librería para realizar solicitudes HTTP)
* Math (librería de matemáticas)
* Time (librería para manejar fechas y horas)
* Json (librería para manipular formatos JSON)
* Signal (librería para manejar señales de sistema)
* Random (librería para generar números aleatorios)

## Configuración de pines

El LED se conectará al pin 17 del GPIO, mientras que el sensor DS18B20 se conectará a los pins 4 y 5.

## Instalación paso a paso

1. Conecta el Raspberry Pi a una fuente de poder.
2. Conecta el LED y el sensor a los pines correspondientes.
3. Descarga e instala las librerías RPi.GPIO, requests, math, time, json, signal y random mediante pip:
```bash
sudo apt-get update
sudo apt-get install python3-pip
pip3 install RPi.GPIO requests math time json signal random
```
4. Clona el repositorio con los archivos de código fuente.

## Uso

1. Abra un terminal en la carpeta donde se encuentra el archivo `blinkled.py`.
2. Ejecute el script utilizando Python 3.x:
```bash
python3 blinkled.py
```
El LED debería encenderse y apagarse cada 0.5 segundos.

## Estructura del proyecto

* El directorio raíz contiene los siguientes archivos:
	+ `blinkled.py`: Script principal para controlar el estado del LED.
	+ `leertempraspy.py`: Script para leer temperatura y enviar datos a Thingspeak.
	+ `thingspeak2_2.py`: Script para interactuar con la plataforma de IoT Thingspeak.
	+ `ubidotsraspi.py`: Script para interactuar con la plataforma de IoT Ubidots.

## Licencia

Este proyecto está bajo la licencia MIT.