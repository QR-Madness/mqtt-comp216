"""
    MQTT Publisher by Group 5
"""
from argparse import ArgumentParser

import paho.mqtt.client as mqtt
import termcolor as tc
from group_5_data_generator import data_generator_g5

arg_parser = ArgumentParser("Group 5 ")
# arg_parser.add_argument("--debug-mode" "-t",
#                         type=argparse.BooleanOptionalAction,
#                         help="Run tests and try to find issues")
arg_parser.add_argument("-p", "--port",
                        type=int,
                        default=1883)
arg_parser.add_argument("-a", "--address",
                        type=str,
                        default="localhost")

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

# TODO: remove debug block
for i in range(5):
    print(data_generator.generate_next())

# free resources
client.disconnect()
