from geopy.distance import geodesic
import paho.mqtt.client as mqtt
import time

def distance():
	ghana = (41.49008, -71.312796)
	cleveland_oh = (41.499498, -81.695391)
	messages = (geodesic(ghana, cleveland_oh).miles)
	return messages

#to check distance


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:
        print("Connection failed")

Connected = False  # global variable for the state of the connection


client = mqtt.Client()
client.on_connect = on_connect
client.connect("10.10.3.221", 1883, 60)
client.loop_start()  # start the loop


while Connected != True:  # Wait for connection
    time.sleep(0.1)


try:
    while True:
        message1 = input('Your message: ')
        message = message1 + str(distance())
        client.publish("Non", message)
        #client.publish(distance())

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()


#def on_connect(client, userdata, flags, rc):
#    print("Connected with result code "+str(rc))

#    while True:
#        message = input('Your message: ')
#        client.publish('#', message)


#client = mqtt.Client()
#client.on_connect = on_connect
#client.loop_forever()