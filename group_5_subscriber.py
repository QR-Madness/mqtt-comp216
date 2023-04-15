import json
import tkinter as tk

import paho.mqtt.client as mqtt


class Subscriber:
    def __init__(self, client_id, broker_address, topic):
        self.client_id = client_id
        self.client = mqtt.Client(self.client_id)
        self.broker_address = broker_address
        self.topic = topic
        self.root = tk.Tk()
        self.client.connect(self.broker_address, 1883, 60)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_connect_fail = self.on_connect_failed

        self.root.title(f"MQTT Subscriber | {self.client_id}")

        self.label_topic = tk.Label(self.root, text="Topic: " + self.topic)
        self.label_message = tk.Label(self.root, text="Message:")
        self.text_message = tk.Text(self.root, wrap=tk.WORD, height=10, width=40)
        self.text_message.config(state=tk.DISABLED)
        self.button_clear = tk.Button(self.root, text="Clear", command=self.clear)

        self.label_topic.grid(row=0, column=0, sticky=tk.W)
        self.label_message.grid(row=1, column=0, sticky=tk.W)
        self.text_message.grid(row=1, column=1, columnspan=2, rowspan=4, sticky=tk.W + tk.E + tk.N + tk.S)
        self.button_clear.grid(row=6, column=0, columnspan=3, pady=5)

        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.label = tk.Label(self.root, text="Received data:")
        self.root.geometry("300x300")
        self.root.after(0, self.run)

    def run(self):

        self.client.loop_start()
        self.root.mainloop()

    def clear(self):
        self.text_message.config(state=tk.NORMAL)  # Enable editing of text_message widget
        self.text_message.delete(1.0, tk.END)
        self.text_message.config(state=tk.DISABLED)  # Set text_message widget as uneditable

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe(self.topic)

    def on_connect_failed(self, client, userdata):
        print(f"{self.client_id} | Failed to connect to the broker")

    def check_corrupted(self, message):
        keys = {
            "location_x": float,
            "location_y": float,
            "location_z": float,
            "date_of_transmittal": str,
            "speed_mps": float
        }

        for key in keys.keys():
            if key not in message.keys():
                return True
            if not isinstance(message[key], keys.get(key)):
                return True
        return False

    def format_message(self, message):
        return f"Retrieved data:\n" \
               f"Timestamp: {message['date_of_transmittal']}\n" \
               f" \n" \
               f"Location:\n " \
               f"   x: {round(message['location_x'], 2)},\n " \
               f"   y: {round(message['location_y'], 2)},\n " \
               f"   z: {round(message['location_z'], 2)};\n" \
               f" \n" \
               f"Speed: {round(message['speed_mps'], 2)} mps"

    def on_message(self, client, userdata, message):
        try:
            data = json.loads(message.payload.decode())
            if self.check_corrupted(data):
                print("Corrupted data found")
                return
            self.text_message.configure(state=tk.NORMAL)
            self.text_message.insert(tk.END, f"{self.format_message(data)}\n------------\n")
            self.text_message.configure(state=tk.DISABLED)
            self.label.config(text=data)
        except:
            print("Invalid message received")


subscriber1 = Subscriber("subscriber1", "localhost", "example/topic1")
subscriber2 = Subscriber("subscriber2", "localhost", "example/topic2")

subscriber1.run()
subscriber2.run()
