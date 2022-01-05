from time import*
import random
import requests
import json
KEY="GZEN53T0T63XDDRJ"#Poner aqui su Key de escritura
KEYREAD="1283406"#Poner aqui su key de lectura

try:
 while True:
  #Escritura de datos a Thingsboard (hacerlo durante 90 segundos)
  value_1 = random.randint(-150, -50)
  value_2 = random.randint(-50, 50)
  value_3 = random.randint(50, 90)
  value_4 = random.randint(90, 150)
  value_5 = random.randint(150, 190)
  value_6 = random.randint(190, 290)
  lista = [value_1,value_2,value_3,value_4,value_5,value_6] 
  ############################################################################################################### Prueba 1
  if len(lista) == 6:
   enviar = requests.get("https://api.thingspeak.com/update?api_key="+KEY+"&field1="+str(lista[0])+"&field2="+str(lista[1])
                                   +"&field3="+str(lista[2])+"&field4="+str(lista[3])+"&field5="+str(lista[4])+"&field6="+str(lista[5]))  #cuando se quiere enviar dos o mas datos
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

 

  #Read data from Thingsboard
  ############################################################################################# Prueba 2
  #recibir = requests.get("https://api.thingspeak.com/channels/"+KEYREAD+"/feeds.json")  ################# NO COMENTAR ESTA LÍNEA DE AQUÍ EN ADELANTE
  """jsonString = json.dumps(recibir.json(),indent=2) 
  print("toda la info es : ")
  print(jsonString)"""
  

  
  ############################################################################################# Prueba 3
  """print("-------------todos los feeds son de las 6 fields------------------------------------")
  jsonString = json.dumps(recibir.json().get("feeds"),indent=2)
  print(jsonString)"""


  
  ############################################################################################# Prueba 4
  #num = 3 if len(recibir.json().get("feeds"))>3 else len(recibir.json().get("feeds"))              ############ NO COMENTAR DE AQUÍ EN ADELANTE
  """print("----Mostrar la info de los primeros 3 valores de los 6 fields----")
  for i in range(num):
   print("*************************************************")
   jsonString = json.dumps(recibir.json().get("feeds")[i],indent=2)
   print(jsonString)
  print("-------Mostrar solo los primeros 3 valores de los 3 primeros fields-------")
  for i in range(num):
   print("*************************************************")
   print("Variable1:",recibir.json().get("feeds")[i].get("field1"))
   print("Variable2:",recibir.json().get("feeds")[i].get("field2"))
   print("Variable3:",recibir.json().get("feeds")[i].get("field3"))"""
  
  ############################################################################################# Prueba 5
  # Asegurarse que la linea 53 no este comentada
  """print("----Mostrar la info de los ultimos 3 valores de las 6 variables-----")
  recibir = requests.get("https://api.thingspeak.com/channels/"+KEYREAD+"/feeds.json?results="+str(num))
  jsonString = json.dumps(recibir.json().get("feeds"),indent=2)
  print(jsonString)
  print("-------Mostrar solo los ultimos 3 valores de las 3 primeros fields-------")
  for i in range(num):
   print("*************************************************")
   print("Variable1:",recibir.json().get("feeds")[i].get("field1"))
   print("Variable2:",recibir.json().get("feeds")[i].get("field2"))
   print("Variable3:",recibir.json().get("feeds")[i].get("field3"))"""
   

  sleep(15)

except KeyboardInterrupt: #Cierra el serial cuando el usuario cierra forzosamente el proceso
	print ("bye")
