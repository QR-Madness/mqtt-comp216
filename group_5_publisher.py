"""
    MQTT Publisher by Group 5
"""
import json
from argparse import ArgumentParser

import paho.mqtt.client as mqtt
import termcolor as tc

from group_5_data_generator import data_generator_g5

arg_parser = ArgumentParser("MQTT -- Group 5 -- Publisher Module")
# arg_parser.add_argument("--debug-mode" "-t",
#                         type=argparse.BooleanOptionalAction,
#                         help="Run tests and try to find issues")
arg_parser.add_argument("-p", "--port",
                        type=int,
                        default=1883)
arg_parser.add_argument("-a", "--address",
                        type=str,
                        default="localhost")
arg_parser.add_argument("-t", "--root-topic",
                        type=str,
                        default="default_ship")

"""
    ----------- MAIN CODE -----------
"""
args = arg_parser.parse_args()
# broker information
broker_port = args.port
broker_address = args.address

# begin program
print(tc.colored("Initiating MQTT publisher...", "blue", attrs=["blink", "reverse"]))

client = mqtt.Client()
data_generator = data_generator_g5()

# attempt a connection to the MQTT broker
try:
    client.connect(broker_address, broker_port)
    if client.is_connected():
        print(tc.colored("[PASS] Connection established to MQTT broker", "green"))

except Exception as e:
    print(tc.colored("[FAIL] Couldn't establish connection to MQTT broker || CAUSE :: \n" + str(e), "red"))

# start send generated packets to broker
try:
    for i in range(5):
        # publish to the topic
        result = client.publish("default_ship/001", json.dumps(data_generator.generate_next().__dict__()))
        if result.is_published():
            print(tc.colored("[Tx]", "green") + " Packet sent to broker.")
        else:
            print(tc.colored("[FAIL Tx] Error sending packet to broker" + result.rc))

except Exception as e:
    print(tc.colored("[FAIL] Data couldn't be published || CAUSE :: \n" + str(e), "red"))

# free resources
client.disconnect()
