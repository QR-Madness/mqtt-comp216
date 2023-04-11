import paho.mqtt.client as mqtt
import termcolor as tc

client = mqtt.Client()

# attempt a connection to the MQTT broker
try:
    client.connect('localhost', 1883)
    if client.is_connected():
        print(tc.colored("[PASS] Connection established to MQTT broker", "green"))
except Exception as e:
    print(tc.colored("[FAIL] Couldn't establish connection to MQTT broker || CAUSE :: \n" + str(e), "red"))

# free resources
client.disconnect()
