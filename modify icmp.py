from scapy.all import *

def send_icmp(target_ip, message):
    # Create an IP packet with the target IP address
    ip = IP(dst=target_ip)

    # Create an ICMP packet with the message
    icmp = ICMP() / message

    # Send the packet
    send(ip/icmp)

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    message = input("Enter the message to send: ")
    send_icmp(target_ip, message)