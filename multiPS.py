import paho.mqtt.client as mqtt
import time
import threading

broker = "localhost"
port = 1883
topic = "test/cpu"

def publish_messages(thread_num):
    client = mqtt.Client()
    client.connect(broker, port, 60)
    print(f"New publisher connected - Thread {thread_num}")
    payload = "cpu"
    try:
        while True:
            client.publish(topic, payload)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(f"Exiting Thread {thread_num}")

def subscribe_messages(thread_num):
    client = mqtt.Client()
    client.connect(broker, port, 60)
    client.subscribe(topic)
    print(f"New subscriber connected - Thread {thread_num}")
    try:
        client.loop_forever() 
    except KeyboardInterrupt:
        print(f"Exiting Thread {thread_num}")

def create_thread(thread_num):
    thread = threading.Thread(target=publish_messages, args=(thread_num,))
    thread.start()
    thread = threading.Thread(target=subscribe_messages, args=(thread_num,))
    thread.start()

if __name__ == "__main__":
    num_threads = 1
    while num_threads < 500:
        create_thread(num_threads)
        time.sleep(0.5)
        num_threads += 1
