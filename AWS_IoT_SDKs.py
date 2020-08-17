#!/usr/bin/python3
import paho.mqtt.client as paho
import os
import socket
import ssl
from time import sleep

connflag = False
 
def on_connect(client, userdata, flags, rc):
    global connflag
    print("Connected to AWS")
    connflag = True
    print("Connection returned result: " + str(rc) )
    # Subscribing in on_connect() means that if we lose the connection and
    client.subscribe("TOPIC" , 1 )       
 
def on_message(client, userdata, msg): 
    print(msg.topic+" "+str(msg.payload))
    #write script for received data in here
 
#def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))
 
mqttc = paho.Client()                      
mqttc.on_connect = on_connect
mqttc.on_message = on_message
#mqttc.on_log = on_log

awshost = "Rest_API"
awsport = 8883                                             
clientId = "Thing_Name"                                    
thingName = "Thing_Name"                                   
caPath = "CA_Path"                           
certPath = "Certificate_Path"                           
keyPath = "private_key_Path" 

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters
mqttc.connect(awshost, awsport, keepalive=60)
mqttc.loop_start()                                         
#mqttc.loop_forever() 

while True:
    if connflag == True:
        #write publish script in here
        mqttc.publish("TOPIC", TOPIC_Value , qos=1)     
        print("msg sent: " +" TOPIC "+ "%.2f" % TOPIC_Value )
    else:
        print("waiting for connection...") 
