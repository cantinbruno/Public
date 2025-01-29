from scapy.all import sniff
from scapy.arch.windows import get_windows_if_list
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.http import HTTPRequest

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = 'Unknown'  
        src_port = dst_port = 'N/A'  
        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            if packet.haslayer(HTTPRequest):  
                protocol = "HTTP"
            else:
                protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        elif ICMP in packet:
            protocol = "ICMP"
        print(f"{ip_src:<20} {src_port:<10} {ip_dst:<20} {dst_port:<10} {protocol:<10}")

def capture_on_interface(iface_name, iface_description):
    print(f"Début de l'écoute sur {iface_description}...")
    print(f"{'IP Source':<20} {'Src Port':<10} {'IP Dest':<20} {'Dst Port':<10} {'Protocol':<10}")
    sniff(iface=iface_name, prn=packet_callback, store=False)

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = 'Unknown'
        src_port = dst_port = 'N/A'
        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        print(f"{ip_src:<20} {src_port:<10} {ip_dst:<20} {dst_port:<10} {protocol:<10}")

def list_interfaces():
    all_interfaces = get_windows_if_list()
    valid_interfaces = [iface for iface in all_interfaces if iface['ips']]
    print("Interfaces réseau actives :")
    for i, iface in enumerate(valid_interfaces, start=1):
        ipv4_addresses = [ip for ip in iface['ips'] if '.' in ip]
        if ipv4_addresses:
            print(f"{i}. {iface['description']} (Adresse IP: {ipv4_addresses[0]})")
            iface['ipv4_address'] = ipv4_addresses[0]
        else:
            print(f"{i}. {iface['description']} (Pas d'adresse IPv4)")
            iface['ipv4_address'] = None
    return valid_interfaces

def main():
    interfaces = list_interfaces()
    if not interfaces:
        print("Aucune interface réseau active n'a été trouvée.")
        return

    while True:
        choice = input("\nChoisissez une interface par numéro (ou 'exit' pour quitter) : ")
        if choice.lower() == 'exit':
            break
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(interfaces):
                    iface_name = interfaces[idx]['name']
                    iface_description = interfaces[idx]['description']
                    capture_on_interface(iface_name, iface_description)
                else:
                    print("Choix invalide. Veuillez réessayer.")
            except ValueError:
                print("Veuillez entrer un numéro valide.")

if __name__ == "__main__":
    main()
