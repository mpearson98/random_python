import platform
import tkinter as tk
from tkinter import scrolledtext
from scapy.all import *

def scan_wifi():
    try:
        networks = []
        if platform.system() == 'Darwin':  # macOS
            # Use scapy to get WiFi information
            wifi = sniff(iface="en0", count=10)
            for packet in wifi:
                if packet.haslayer(Dot11Beacon):
                    networks.append(packet.info)
        else:  # Linux
            # Use scapy to get WiFi information
            wifi = sniff(iface="wlan0", count=10)
            for packet in wifi:
                if packet.haslayer(Dot11Beacon):
                    networks.append(packet.info)
        return '\n'.join(networks)
    except Exception as e:
        return f"An error occurred: {e}"

def update_text():
    text.delete('1.0', tk.END)
    text.insert(tk.INSERT, scan_wifi())

root = tk.Tk()
root.title("WiFi Monitor")

text = scrolledtext.ScrolledText(root, width=70, height=30)
text.pack()

button = tk.Button(root, text="Refresh", command=update_text)
button.pack()

root.mainloop()