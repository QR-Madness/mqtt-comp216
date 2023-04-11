import tkinter as tk


class SubscriberUI:
    def __init__(self, master):
        self.master = master
        self.master.title("MQTT Subscriber")

        self.label_topic = tk.Label(self.master, text="Topic:")
        self.label_message = tk.Label(self.master, text="Message:")
        self.variable_topic = tk.StringVar(self.master)
        self.dropdown_topic = tk.OptionMenu(self.master, self.variable_topic, "topic1", "topic2", "topic3")
        self.text_message = tk.Text(self.master, wrap=tk.WORD, height=10, width=40)
        self.text_message.config(state=tk.DISABLED)  
        self.button_subscribe = tk.Button(self.master, text="Subscribe", command=self.subscribe)
        self.button_clear = tk.Button(self.master, text="Clear", command=self.clear)

        self.label_topic.grid(row=0, column=0, sticky=tk.W)
        self.label_message.grid(row=1, column=0, sticky=tk.W)
        self.dropdown_topic.grid(row=0, column=1, columnspan=2, sticky=tk.W + tk.E + tk.N + tk.S)
        self.text_message.grid(row=1, column=1, columnspan=2, rowspan=4, sticky=tk.W + tk.E + tk.N + tk.S)
        self.button_subscribe.grid(row=5, column=0, columnspan=3, pady=10)
        self.button_clear.grid(row=6, column=0, columnspan=3, pady=5)

        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(4, weight=1)

        # THE Following are mqtt codes
        # self.client = mqtt.Client()
        # self.client.on_message = self.on_message_received

    # This is the Callback function for handling received MQTT messages
    def on_message_received(self, client, userdata, msg):
        # Update the text_message Text widget with the received message
        self.text_message.config(state=tk.NORMAL)  
        self.text_message.insert(tk.END, f"{msg.topic}: {msg.payload.decode('utf-8')}\n")
        self.text_message.config(state=tk.DISABLED)  

    def subscribe(self):
        topic = self.variable_topic.get()
        self.client.subscribe(topic)

    def clear(self):
        self.text_message.config(state=tk.NORMAL)  # Enable editing of text_message widget
        self.text_message.delete(1.0, tk.END)
        self.text_message.config(state=tk.DISABLED)  # Set text_message widget as uneditable


if __name__ == "__main__":
    root = tk.Tk()
    subscriber_ui = SubscriberUI(root)
    root.mainloop()
