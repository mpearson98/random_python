import subprocess
import platform
import tkinter as tk
from tkinter import scrolledtext

def scan_wifi():
    try:
        if platform.system() == 'Darwin':  # macOS
            command = ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-s']
        else:  # Linux
            command = ['nmcli', '-t', 'dev', 'wifi']

        # Run the command to scan for WiFi networks
        result = subprocess.run(command, stdout=subprocess.PIPE, universal_newlines=True)

        # Return the result
        return result.stdout
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