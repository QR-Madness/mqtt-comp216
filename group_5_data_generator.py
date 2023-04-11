# basic data packet
import datetime
from random import random


class DataTransmitPacket:
    """ 'Template' class for the data packets. """

    # random data generation constraints
    coord_max = 50000
    vector_max_source = 1000
    vector_max_target = 1000
    speed_max = 1000

    # contents
    location_x: float
    location_y: float
    location_z: float
    rotation_vector: str
    speed_mps: float
    date_of_transmittal: datetime

    def __init__(self):
        # randomize location coordinates with a max value cmax
        self.location_x = random() * self.coord_max
        self.location_y = random() * self.coord_max
        self.location_z = random() * self.coord_max
        # randomize rotation vector in format 'ST-> = {x2 - x1, y2 - y1, z2 - z1}'
        self.rotation_vector = "{ t2=" + str(random() * self.vector_max_source) + ", s1= " "}"
        self.speed_mps = random() * self.speed_max
        self.date_of_transmittal = datetime.datetime.now()

    def __str__(self):
        return "POSITION==(" + self.location_x.__str__() + ", " + self.location_y.__str__() + ", " + self.location_z.__str__() + ")"


class data_generator_g5:
    """
        Generates random values for the MQTT publisher.
    """
    packet_generate_count = 0

    def __init__(self):
        pass

    def generate_next(self):
        """
        :return Data packet dictionary containing generated values.
        """
        self.packet_generate_count += 1
        return DataTransmitPacket()
