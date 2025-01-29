import subprocess
import platform
from ipaddress import ip_network
from concurrent.futures import ThreadPoolExecutor
import dns.resolver
import dns.reversename
from tabulate import tabulate
import socket
from scapy.all import ARP, Ether, srp

COMMON_PORTS = {
    20: 'FTP-DT',
    21: 'FTP-CC',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    465: 'SMTPS',
    587: 'SMTPS',
    993: 'IMAPS',
    995: 'POP3S',
    3306: 'MySQL',
    3389: 'RDP',
    5900: 'VNC',
    8080: 'HTTP-Alt'
}

def ping_host(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    creationflags = subprocess.CREATE_NO_WINDOW if platform.system().lower() == 'windows' else 0
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=creationflags)
    if platform.system().lower() == 'windows':
        return "TTL=" in result.stdout.decode('cp1252', errors='ignore')
    else:
        return "1 packets received" in result.stdout.decode('cp1252', errors='ignore') or "1 received" in result.stdout.decode('cp1252', errors='ignore')

def get_hostname(ip):
    resolver = dns.resolver.Resolver()
    resolver.timeout = 5
    resolver.lifetime = 5
    try:
        addr = dns.reversename.from_address(ip)
        answers = resolver.resolve(addr, "PTR")
        return str(answers[0].target).rstrip('.')
    except (dns.resolver.NXDOMAIN, dns.resolver.Timeout, dns.exception.DNSException):
        return 'Inconnu'

def get_mac(ip):
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)
    answered, _ = srp(arp_request, timeout=2, retry=1, verbose=False)
    for sent, received in answered:
        return received.hwsrc
    return "Inconnu"

def check_host(ip_str):
    is_up = ping_host(ip_str)
    mac = get_mac(ip_str) if is_up else 'N/A'
    hostname = get_hostname(ip_str) if is_up else 'Hors ligne'
    status = 'Up' if is_up else 'Down'
    open_ports = [(port, scan_port(ip_str, port)) for port in COMMON_PORTS.keys() if scan_port(ip_str, port)]
    return ip_str, hostname, status, mac, open_ports

def scan_network(network_cidr, max_workers=100):
    network = ip_network(network_cidr)
    ips = [str(ip) for ip in network.hosts()]
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(check_host, ips))
    sorted_results = sorted(results, key=lambda x: int(ip_network(x[0]).network_address))
    table_data = []
    for ip, hostname, status, mac, open_ports in sorted_results:
        services = [f"{port}/{COMMON_PORTS[port]}" for port, is_open in open_ports if is_open]
        table_data.append([ip, hostname, status, mac, ', '.join(services)])
    print(tabulate(table_data, headers=['Adresse IP', 'Nom d’hôte', 'Statut', 'MAC', 'Services Ouverts'], tablefmt='grid'))

def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect((ip, port))
            return True
        except (socket.timeout, socket.error):
            return False

if __name__ == "__main__":
    network_cidr = input("Veuillez entrer le réseau CIDR (ex: '192.168.1.0/24'): ")
    scan_network(network_cidr)

input("\nAppuyez sur Entrée pour terminer le script.")
