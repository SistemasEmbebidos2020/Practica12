
from time import*
import requests
import math
import random
    
TOKEN = "BBFF-eosbgxCNNDPfdhbvzWijMQFC9FIAvS"  # Put your TOKEN here
DEVICE_LABEL = "practica13"  # Put your device label here 
VARIABLE_LABEL_1 = "temperature"  # Put your first variable label here
VARIABLE_LABEL_2 = "humidity"  # Put your second variable label here
VARIABLE_LABEL_3 = "position"  # Put your second variable label here


def build_payload(variable_1, variable_2, variable_3):
    # Creates two random values for sending data
    value_1 = random.randint(-50, 90)
    value_2 = random.randint(0, 100)
    print ("CONECTADO...")  
    

    # Creates a random gps coordinates
    lat = random.randrange(34, 36, 1) + \
    random.randrange(1, 1000, 1) / 1000.0
    lng = random.randrange(-83, -87, -1) + \
    random.randrange(1, 1000, 1) / 1000.0

    payload = {variable_1: value_1,
              variable_2: value_2,
              variable_3: {"value": 1, "context": {"lat": lat, "lng": lng}}}

    return payload


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        sleep(1)

    # Processes results
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True



while(1):    
    payload = build_payload(
    VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3)
    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")
    sleep(10)



