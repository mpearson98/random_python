import subprocess
import time

def monitor_wifi(network_name):
    try:
        # Run the command to get the WiFi signal quality
        result = subprocess.run(['iwconfig'], stdout=subprocess.PIPE, universal_newlines=True)

        # Find the line with the network name
        lines = result.stdout.split('\n')
        for line in lines:
            if network_name in line:
                # Extract the signal quality
                quality = line.split('Signal level=')[1]
                return quality
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def generate_report(network_name, quality_list):
    with open('wifi_report.txt', 'w') as f:
        f.write(f"Report for network: {network_name}\n")
        for i, quality in enumerate(quality_list):
            f.write(f"Time: {i} sec, Signal Quality: {quality}\n")

if __name__ == "__main__":
    network_name = 'MJPHOTEL'
    quality_list = []
    for i in range(60):  # Monitor for 60 seconds
        quality = monitor_wifi(network_name)
        if quality:
            quality_list.append(quality)
        time.sleep(1)
    generate_report(network_name, quality_list)