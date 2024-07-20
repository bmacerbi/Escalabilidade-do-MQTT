import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("test/payload")

def on_message(client, userdata, msg):
    print(f"Received message of length {len(msg.payload.decode())}")

broker = "localhost"
port = 1883
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)
client.loop_forever()
