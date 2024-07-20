import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topic = "test/payload"
client = mqtt.Client()

client.connect(broker, port, 60)

payload = "a"
try:
    while True:
        client.publish(topic, payload)
        print(f"Sent payload of length {len(payload)}")
        payload += "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
except KeyboardInterrupt:
    print("Exiting")
