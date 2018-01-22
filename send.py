#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue = 'data')
channel.basic_publish(exchange = '', routing_key = 'data', body = 'Temperature: Fucking Warm')

print(" [x] Sent 'Temperature: Fucking Warm'")

connection.close()
