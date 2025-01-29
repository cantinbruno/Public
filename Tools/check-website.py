import socket
import ssl
import whois
import requests
import dns.resolver
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def get_dns_records(domain):
    records = {
        "A": [],
        "MX": [],
        "NS": [],
        "TXT": [],
        "CNAME": []
    }
    for record_type in records.keys():
        try:
            dns_data = dns.resolver.resolve(domain, record_type)
            for data in dns_data:
                records[record_type].append(data.to_text())
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            continue
    return records

def get_certificate_details(domain):
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=domain) as sock:
            sock.connect((domain, 443))
            cert = sock.getpeercert()
        return cert
    except Exception as e:
        return str(e)

def get_http_security_headers(url):
    try:
        headers = requests.get(url).headers
        security_headers = {
            'Strict-Transport-Security': headers.get('Strict-Transport-Security'),
            'X-Frame-Options': headers.get('X-Frame-Options'),
            'X-Content-Type-Options': headers.get('X-Content-Type-Options'),
            'Content-Security-Policy': headers.get('Content-Security-Policy'),
            'X-XSS-Protection': headers.get('X-XSS-Protection'),
        }
        return security_headers
    except requests.RequestException as e:
        return str(e)

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return str(e)

def format_certificate_details(cert):
    formatted_cert = {}
    for key, value in cert.items():
        if isinstance(value, tuple):
            formatted_value = ", ".join(f"{val[0]}={val[1]}" if len(val) > 1 else str(val[0]) for val in value)
        elif isinstance(value, list):
            formatted_value = ", ".join(", ".join(f"{val[0]}={val[1]}" if len(val) > 1 else str(val[0]) for val in sublist) if isinstance(sublist, tuple) else str(sublist) for sublist in value)
        else:
            formatted_value = value
        formatted_cert[key] = formatted_value
    return formatted_cert


def print_info(title, info):
    table = Table(title=title, box=box.SIMPLE_HEAD)
    table.add_column("Key", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    if isinstance(info, dict):
        for key, value in info.items():
            if isinstance(value, (list, tuple)):
                value = "\n".join(str(v) for v in value)
            elif not isinstance(value, str):
                value = str(value)
            table.add_row(key, value)
    elif not isinstance(info, str):
        info = str(info)
        table.add_row(title, info)
    console.print(table)

def main(url):
    console.print(f"Analyzing URL: [underline]{url}[/underline]\n", style="bold")

    domain = url.split("//")[-1].split("/")[0]
    console.print(f"Domain: {domain}\n", style="bold underline")

    dns_records = get_dns_records(domain)
    print_info("DNS Records", dns_records)

    cert_details = get_certificate_details(domain)
    formatted_cert_details = format_certificate_details(cert_details)
    print_info("SSL Certificate Details", formatted_cert_details)

    security_headers = get_http_security_headers(url)
    print_info("HTTP Security Headers", security_headers)

    whois_info = get_whois_info(domain)
    print_info("WHOIS Information", whois_info)

if __name__ == "__main__":
    url_input = console.input("Enter the website URL (with https:// ): ")
    main(url_input)
