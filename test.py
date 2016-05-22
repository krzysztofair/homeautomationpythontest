import requests
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
	requests.post('http://192.168.0.16/laravel/public/index.php/api/subscribe', data = { 'topic':msg.topic,'body':str(msg.payload)})
	print(msg.topic+" "+str(msg.payload))

def on_connect(client, userdata, flags, rc):

	print("Connected with result " +str(rc))
	client.subscribe("#")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.16", 1883)

client.loop_forever()


