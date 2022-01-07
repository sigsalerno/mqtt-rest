import paho.mqtt.client as mqtt
import json 
import requests
import os

import logging 
logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    logging.info("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(os.environ['MQTT_TOPIC'])

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    
    try:
        payload = json.loads(msg.payload)

        url = os.environ['API_URL']

        logging.info(msg.topic+" "+str(msg.payload))

        res = requests.post(url, payload, headers={'Content-Type': 'application/json'})
        
        logging.info("Response: "+str(res.text))

    except json.decoder.JSONDecodeError:
        logging.error(msg.topic+" "+str(msg.payload)+"JSON payload not valid")

if __name__ == "__main__":

    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message

    
    client.connect(os.environ['MQTT_SERVER'], int(os.environ['MQTT_SERVER_PORT']), 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()