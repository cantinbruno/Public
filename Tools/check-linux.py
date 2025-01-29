#!/bin/bash

print_header() {
    echo -e "\n======================================================================"
    echo -e " $1"
    echo -e "======================================================================"
}

get_system_info() {
    print_header "Informations système"
    echo "Nom de l'ordinateur: $(hostname)"
    echo "Modèle: $(sudo dmidecode -s system-product-name)"
    echo "Type de PC: $(sudo dmidecode -s system-manufacturer)"
    echo "Nombre de processeurs: $(nproc)"
    echo "Utilisateur actuel: $USER"
    echo "Mémoire physique: $(free -h --si | awk '/Mem/{print $2}')"
}

get_os_info() {
    print_header "Informations système d'exploitation"
    echo "Nom: $(lsb_release -d | cut -f2)"
    echo "Version: $(lsb_release -r | cut -f2)"
    echo "Architecture: $(uname -m)"
    echo "Dernier redémarrage: $(uptime -s)"
}

get_bios_info() {
    print_header "Informations BIOS"
    echo "Fabricant: $(sudo dmidecode -s bios-vendor)"
    echo "Version: $(sudo dmidecode -s bios-version)"
}

get_disk_info() {
    print_header "Informations sur le disque"
    sudo fdisk -l | grep "Disk /dev" | awk '{print "Modèle: " $2, $3, $4; system("echo Taille: " $5)}'
}

get_gpu_info() {
    print_header "Informations sur les cartes graphiques"
    echo "Nom: $(lspci | grep VGA | cut -d ':' -f3)"
    echo "Description: $(lspci | grep VGA | cut -d ':' -f3)"
}

get_network_info() {
    print_header "Configuration réseau"
    echo "Adresse IP: $(hostname -I)"
    echo "Adresse MAC: $(ip link | awk '/ether/{print $2}' | head -n 1)"
    echo "Passerelle par défaut: $(ip route | grep default | awk '{print $3}')"
}

get_processor_info() {
    print_header "Informations sur le processeur"
    echo "Nom: $(grep -m 1 'model name' /proc/cpuinfo | cut -d ':' -f2)"
    echo "Nombre de cœurs: $(grep -c 'processor' /proc/cpuinfo)"
    echo "Vitesse d'horloge: $(grep -m 1 'cpu MHz' /proc/cpuinfo | cut -d ':' -f2)"
}

get_memory_info() {
    print_header "Informations sur la mémoire RAM"
    echo "Capacité totale: $(grep -m 1 'MemTotal' /proc/meminfo | awk '{print $2/1024/1024}') GB"
    echo "Mémoire disponible: $(grep -m 1 'MemAvailable' /proc/meminfo | awk '{print $2/1024/1024}') GB"
}

get_running_services() {
    print_header "Services Linux en cours d'exécution"
    sudo service --status-all | grep "+"
}

get_installed_software() {
    print_header "Logiciels installés"
    dpkg -l | grep ii | awk '{print "Nom: " $2 ", Version: " $3}'
}

main() {
    get_system_info
    get_os_info
    get_bios_info
    get_disk_info
    get_gpu_info
    get_processor_info
    get_memory_info
    get_network_info
    get_installed_software
    get_running_services
}

main
read -p $'\nAppuyez sur Entrée pour terminer le script.'
