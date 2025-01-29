import nmap
from rich.console import Console
from rich.table import Table

def print_scan_results(nm, console):
    for host in nm.all_hosts():
        table = Table(show_header=True)
        table.add_column("Port", width=12)
        table.add_column("Service", width=12)
        table.add_column("Scripts & Output", min_width=20)

        console.print(f'Host : {host} ({nm[host].hostname()})')
        console.print(f'State : {nm[host].state()}')

        for proto in nm[host].all_protocols():
            console.print(f'----------\nProtocol : {proto}')
            lport = sorted(nm[host][proto].keys())
            for port in lport:
                service_info = nm[host][proto][port]
                scripts_outputs = "\n".join([f'{script}: {output}' for script, output in service_info.get('script', {}).items()])
                table.add_row(str(port), service_info["name"], scripts_outputs)

            console.print(table)

def scan_for_vulnerabilities(ip_address, console):
    nm = nmap.PortScanner()
    nm.scan(ip_address, arguments='-sV --script=vuln -T3 -vv')
    print_scan_results(nm, console)

if __name__ == "__main__":
    console = Console()
    target = console.input("Veuillez entrer l'adresse IP à scanner : ")
    scan_for_vulnerabilities(target, console)

    console.input("\nAppuyez sur Entrée pour terminer le script.")
