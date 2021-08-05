
from time import*
import random
import requests
import json

try:
 while True:
  #Escritura de datos a Thingsboard
  value_1 = random.randint(-150, -50)
  value_2 = random.randint(-50, 50)
  value_3 = random.randint(50, 90)
  value_4 = random.randint(90, 150)
  value_5 = random.randint(150, 190)
  value_6 = random.randint(190, 290)
  lista = [value_1,value_2,value_3,value_4,value_5,value_6] 
  ###############################################################################################################
  if len(lista) == 6:
   enviar = requests.get("https://api.thingspeak.com/update?api_key=B3ZRHNV2DUMV48XB&field1="+str(lista[0])+"&field2="+str(lista[1])
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
  sleep(15)


  #Read data from Thingsboard
  #############################################################################################
  recibir = requests.get("https://api.thingspeak.com/channels/1054295/feeds.json")
  jsonString = json.dumps(recibir.json(),indent=2) 
  print("toda la info es : ")
  print(jsonString)
  

  
  #############################################################################################
  """print("-------------todos los feeds son------------------------------------")
  jsonString = json.dumps(recibir.json().get("feeds"),indent=2)
  print(jsonString)"""


  
  #############################################################################################
  """print("----Mostrar la info de los primeros 3 valores----")
  num = 3 if len(recibir.json().get("feeds"))>3 else len(recibir.json().get("feeds"))              ############ NO COMENTAR PORQUE SE USA EN LINEA 60
  for i in range(num):
   print("*************************************************")
   jsonString = json.dumps(recibir.json().get("feeds")[i],indent=2)
   print(jsonString)

  print("-------Mostrar solo los primeros 3 valores-------")
  for i in range(num):
   print("*************************************************")
   print("Variable1:",recibir.json().get("feeds")[i].get("field1"))
   print("Variable2:",recibir.json().get("feeds")[i].get("field2"))
   print("Variable3:",recibir.json().get("feeds")[i].get("field3"))

  
  #############################################################################################
  print("----Mostrar la info de los ultimos 3 valores-----")
  recibir = requests.get("https://api.thingspeak.com/channels/1054295/feeds.json?results="+str(num))
  jsonString = json.dumps(recibir.json().get("feeds"),indent=2)
  print(jsonString)
  print("-------Mostrar solo los ultimos 3 valores-------")
  for i in range(num):
   print("*************************************************")
   print("Variable1:",recibir.json().get("feeds")[i].get("field1"))
   print("Variable2:",recibir.json().get("feeds")[i].get("field2"))
   print("Variable3:",recibir.json().get("feeds")[i].get("field3"))"""
   


  sleep(15)

except KeyboardInterrupt: #Cierra el serial cuando el usuario cierra forzosamente el proceso
	print ("bye")
	
