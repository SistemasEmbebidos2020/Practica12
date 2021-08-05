
from time import*
import random
import requests

try:
 while True:
  #Escritura de datos a Thingsboard
  value_1 = random.randint(-50, 90)
  value_2 = random.randint(-50, 90)
  lista = [value_1,value_2] 
  if len(lista) == 2:
   enviar = requests.get("https://api.thingspeak.com/update?api_key=B3ZRHNV2DUMV48XB&field1="+str(lista[0])+"&field2="+str(lista[1]))  #cuando se quiere enviar dos o mas datos
   #enviar = requests.get("https://api.thingspeak.com/update?api_key=B3ZRHNV2DUMV48XB&field1="+str(lista[0]))
   if enviar.status_code == requests.codes.ok:
     if enviar.text != '0':
      print("Datos enviados correctamente")
     else:
      print("Tiempo de espera insuficiente (>15seg)")
   else:
     print("Error en el request: ",enviar.status_code)
	 #else:
	 #print("La cadena recibida no contiene 2 elementos, sino:",len(lista),"elementos")
  sleep(15)

except KeyboardInterrupt: #Cierra el serial cuando el usuario cierra forzosamente el proceso
	print ("bye")
	
