import platform
import tkinter as tk
from tkinter import scrolledtext
from wifi import Cell, Scheme
from objc_util import ObjCClass

def scan_wifi():
    try:
        if platform.system() == 'Darwin':  # macOS
            networks = []
            # Use CWInterface to get WiFi information
            CWInterface = ObjCClass('CWInterface')
            interface = CWInterface.interface()
            for network in interface.scanForNetworksWithName_error_(None, None):
                networks.append(f"{network.ssid()} - {network.rssiValue()}")
            return '\n'.join(networks)
        else:  # Linux
            # Use wifi library to get WiFi information
            cells = Cell.all('wlan0')
            return '\n'.join([f"{cell.ssid} - {cell.signal}" for cell in cells])
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