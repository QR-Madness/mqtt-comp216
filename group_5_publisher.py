import json
import random
import time

import paho.mqtt.client as mqtt

from group_5_data_generator import data_generator_g5


class Publisher:
    def __init__(self, address, port, topic, generator=data_generator_g5()):
        self.address = address
        self.port = port
        self.topic = topic
        self.client = mqtt.Client()
        self.client.connect(self.address, self.port)
        self.generator = generator

    def should_fail(self):
        return random.randint(0, 100) == 1

    def should_corrupt(self):
        return random.uniform(0, 100) < 0.5

    def publish(self):
        if self.should_fail():
            pass
        if self.should_corrupt():
            value = json.dumps({
                "corrupted": 0.1
            })
        else:
            value = self.generator.generate_next()
        self.client.publish(self.topic, value)
        print("[SENT] :: " + self.topic + " DUMP::" + value)


# Define the main function for generating and publishing the sensor data
def main():
    publisher1 = Publisher("localhost", 1883, "example/topic1")
    publisher2 = Publisher("localhost", 1883, "example/topic2")
    while True:
        publisher1.publish()
        publisher2.publish()
        time.sleep(0.1)


if __name__ == '__main__':
    main()
