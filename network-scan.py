from scapy.all import ARP, Ether, srp
from ipaddress import ip_network

def scan_network(network):
    # Create an ARP request packet
    arp = ARP(pdst=str(network))

    # Create an Ethernet frame
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    # Send the packet and capture the response
    result = srp(ether/arp, timeout=3, verbose=0)[0]

    # List to hold the IP and MAC address of active hosts
    active_hosts = []

    for sent, received in result:
        active_hosts.append({'IP': received.psrc, 'MAC': received.hwsrc})

    return active_hosts

if __name__ == "__main__":
    network = ip_network(input("Enter the network (e.g., 192.168.1.0/24): "))
    active_hosts = scan_network(network)
    for host in active_hosts:
        print(f"IP: {host['IP']}, MAC: {host['MAC']}")