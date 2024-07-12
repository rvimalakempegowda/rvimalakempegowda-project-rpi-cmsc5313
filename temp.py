import time 
import Freenove_DHT as DHT 

import firebase_setup
import constant

DHTPin = 11


collection = firebase_setup.db.collection(constant.COLLECTION_NAME)
doc_Temperature_humidity_ref = collection.document(constant.DOCUMENT_TEMPERATURE)


def uploadFirebase(temperature, humidity, preTempreature , preHumidity):
    if(preHumidity != humidity or preTempreature !=temperature):
        print('uploading') 
        doc_Temperature_humidity_ref.update({u'temp': temperature,'humidity':humidity})  
    return temperature, humidity


def temperature_humidity():
    preHumidity = 0
    preTempreature = 0
    dht = DHT.DHT(DHTPin)   #create a DHT class object 
    for i in range(0,15):             
        chk = dht.readDHT11()     
        if (chk == dht.DHTLIB_OK):      
            # print("DHT11,OK!") 
            break
            
    temperature = round((dht.temperature),1)
    humidity = int(round((dht.humidity),0))
    preTempreature,preHumidity  = uploadFirebase(temperature, humidity, preTempreature , preHumidity)
    print("Pre Humidity: ", preHumidity)
    print("Pre Temperature: ", preTempreature) 