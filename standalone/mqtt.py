from paho.mqtt import client as mqtt_client
import logging
logger = logging.getLogger('mqtt')


def connect_mqtt(client_id, username, password, broker, on_connect, port = 1883, background = False):
    def on_connect_mqtt(client, userdata, flags, rc):
        if rc == 0:
            logger.info("Connected to MQTT Broker!")
            on_connect(client, userdata, flags, rc)
        else:
            logger.error("Failed to connect, return code %d\n", rc)
            quit()
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.reconnect_delay_set(min_delay=1, max_delay=30)
    client.on_connect = on_connect_mqtt

    if background == True:
        client.loop_start()
        client.connect(broker, port)
        return client
    else:
        client.connect(broker, port)
        client.loop_forever()
    