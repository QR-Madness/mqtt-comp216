"""
    MQTT Publisher by Group 5
"""
from argparse import ArgumentParser

import paho.mqtt.client as mqtt
import termcolor as tc

arg_parser = ArgumentParser("Group 5 ")
# arg_parser.add_argument("--debug-mode" "-t",
#                         type=argparse.BooleanOptionalAction,
#                         help="Run tests and try to find issues")
arg_parser.add_argument("--broker-port" "-p",
                        type=int,
                        default=1883)
arg_parser.add_argument("--broker-address" "-a",
                        type=str,
                        default="localhost")

"""
    ----------- MAIN CODE -----------
"""
args = arg_parser.parse_args()
# broker information
broker_port = args.p
broker_address = args.a

# begin program
print("Initiating MQTT publisher...")

client = mqtt.Client()

# attempt a connection to the MQTT broker
client.connect(broker_address, broker_port)
if client.is_connected():
    print(tc.colored("[PASS] Connection established to MQTT broker", "green"))
else:
    print(tc.colored("[FAIL] Couldn't establish connection to MQTT broker || ERROR :: ", "red"))

# free resources
client.disconnect()
