import subprocess

def scan_wifi():
    try:
        # Run the command to scan for WiFi networks
        result = subprocess.run(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-s'], stdout=subprocess.PIPE, universal_newlines=True)

        # Print the result
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scan_wifi()