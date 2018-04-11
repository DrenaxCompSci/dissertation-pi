#!/usr/bin/env python
import serial # for Arduino communication
import time
import paho.mqtt.client as mqtt # for MQTT connection

ser = serial.Serial('/dev/ttyACM0', 9600)
mqtt_host = "192.168.10.124"
mqtt_topic = "dataTopic"

# mqtt setup
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected to: ", mqtt_host)
    
client.on_connect = on_connect
client.connect(mqtt_host, 1883)
    
while True:
    currentPacket = ser.readline()
    print("Sent data...")
    print(currentPacket)
    client.publish(mqtt_topic, currentPacket, 0, False)
    time.sleep(1)

client.loop_forever()
client.disconnect()