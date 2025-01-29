import subprocess
import platform
import psutil
import socket
import os
import wmi
from datetime import datetime
import getpass

def print_header(header):
    print("\n" + "=" * 100)
    print(header.upper())
    print("=" * 100)

def get_system_info():
    c = wmi.WMI()
    print_header("Informations système")
    for system in c.Win32_ComputerSystem():
        print(f"Nom de l'ordinateur: {system.Name}")
        print(f"Modèle: {system.Model}")
        print(f"Type de PC: {system.SystemType}")
        print(f"Nombre de processeurs: {system.NumberOfProcessors}")
    for os_info in c.Win32_OperatingSystem():
        print(f"Utilisateur actuel: {getpass.getuser()}")
        total_mem_gb = float(os_info.TotalVisibleMemorySize) / 1_048_576
        print(f"Mémoire physique: {total_mem_gb:.2f} GB")

def get_os_info():
    c = wmi.WMI()
    print_header("Informations système d'exploitation")
    for os_info in c.Win32_OperatingSystem():
        print(f"Nom: {os_info.Caption}")
        print(f"Version: {os_info.Version}")
        print(f"Architecture: {os_info.OSArchitecture}")
        last_boot_time = datetime.strptime(os_info.LastBootUpTime.split('.')[0], '%Y%m%d%H%M%S')
        print(f"Dernier redémarrage: {last_boot_time.strftime('%d/%m/%Y %H:%M:%S')}")

def get_bios_info():
    c = wmi.WMI()
    print_header("Informations BIOS")
    for bios in c.Win32_BIOS():
        print(f"Fabricant: {bios.Manufacturer}")
        print(f"Nom: {bios.Name}")
        print(f"Version: {bios.Version}")

def get_disk_info():
    c = wmi.WMI()
    print_header("Informations sur le disque")
    for disk in c.Win32_DiskDrive():
        disk_size_gb = float(disk.Size) / 1_073_741_824
        print(f"Modèle: {disk.Model}")
        print(f"Taille: {disk_size_gb:.2f} GB")

def get_gpu_info():
    c = wmi.WMI()
    print_header("Informations sur le GPU")
    for gpu in c.Win32_VideoController():
        print(f"Nom: {gpu.Name}")
        print(f"Statut: {gpu.Status}")
        print(f"Description: {gpu.Description}")

def get_processor_info():
    c = wmi.WMI()
    print_header("Informations sur le processeur")
    for processor in c.Win32_Processor():
        print(f"Nom: {processor.Name}")
        print(f"Nombre de cœurs: {processor.NumberOfCores}")
        print(f"Vitesse d'horloge: {processor.MaxClockSpeed} MHz")

def get_memory_info():
    c = wmi.WMI()
    print_header("Informations sur la mémoire RAM")
    for memory in c.Win32_ComputerSystem():
        total_memory_gb = int(memory.TotalPhysicalMemory) / (1024 ** 3)
        available_memory_gb = psutil.virtual_memory().available / (1024 ** 3)
        print(f"Capacité totale: {total_memory_gb:.2f} Go")
        print(f"Mémoire disponible: {available_memory_gb:.2f} Go")

def get_network_info():
    c = wmi.WMI()
    print_header("Informations réseau")
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        print(f"Description: {interface.Description}")
        print(f"Adresse MAC: {interface.MACAddress}")
        if isinstance(interface.IPAddress, list):
            print(f"Adresse IP: {', '.join(interface.IPAddress)}")
        else:
            print(f"Adresse IP: {interface.IPAddress}")
        if interface.IPSubnet:
            if isinstance(interface.IPSubnet, list):
                print(f"Masque de sous-réseau: {', '.join(interface.IPSubnet)}")
            else:
                print(f"Masque de sous-réseau: {interface.IPSubnet}")
        if interface.DefaultIPGateway:
            if isinstance(interface.DefaultIPGateway, list):
                print(f"Passerelle par défaut: {', '.join(interface.DefaultIPGateway)}")
            else:
                print(f"Passerelle par défaut: {interface.DefaultIPGateway}")

def get_running_services():
    c = wmi.WMI()
    print_header("Services Windows en cours d'exécution")
    for service in c.Win32_Service(State='Running'):
        print(f"Nom: {service.Name}, État: {service.State}")

def get_installed_software():
    c = wmi.WMI()
    print_header("Logiciels installés")
    for software in c.Win32_Product():
        print(f"Nom: {software.Name}, Version: {software.Version}")

def main():
    if 'wmi' not in globals():
        print("Certaines fonctionnalités ne seront pas disponibles car le module 'wmi' n'est pas installé.")
        return
    get_system_info()
    get_os_info()
    get_bios_info()
    get_disk_info()
    get_gpu_info()
    get_processor_info()
    get_memory_info()
    get_network_info()
    get_running_services()
    get_installed_software()
    input("\nAppuyez sur Entrée pour terminer le script.")

if __name__ == "__main__":
    main()
