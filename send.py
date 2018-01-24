#!/usr/bin/env python
import pika # for RabbitMQ
import serial # for Arduino communication

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue = 'data')

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    currentPacket = ser.readline()
    channel.basic_publish(exchange = '', routing_key = 'data', body = currentPacket)
    print(" [x] Sent data")

connection.close()
