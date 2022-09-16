# python3.6

import random

from paho.mqtt import client as mqtt_client


broker = "broker.emqx.io"
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f"python-mqtt-{random.randint(0, 100)}"
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"


# > The function `connect_mqtt()` connects to the MQTT broker and returns a client object
# :return: A client object
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


# It subscribes to the `topic` and prints the message payload when it receives a message
# :param client: the client instance for this callback
# :type client: mqtt_client
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


# `run()` connects to the MQTT broker, subscribes to the topic `/sensors/temperature`, and then loops
# forever, waiting for messages.
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == "__main__":
    run()
