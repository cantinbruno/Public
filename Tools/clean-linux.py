import os
import subprocess

def nettoyage_disque():
    print("Exécution du nettoyage de disque...")
    subprocess.call("sudo apt-get clean", shell=True)

def nettoyage_temp():
    print("Suppression des fichiers temporaires...")
    subprocess.call("sudo rm -rf /tmp/*", shell=True)

def nettoyage_dns():
    print("Nettoyage du cache DNS...")
    subprocess.call("sudo systemd-resolve --flush-caches", shell=True)

def nettoyage_arp():
    print("Nettoyage du cache ARP...")
    subprocess.call("sudo ip -s -s neigh flush all", shell=True)

def verification_systeme():
    print("Vérification de l'intégrité des fichiers système...")
    subprocess.call("sudo fsck -a", shell=True)

def mise_a_jour():
    print("Mise à jour du système...")
    subprocess.call("sudo apt-get update && sudo apt-get upgrade -y", shell=True)

def redemarrer():
    print("Redémarrage de l'ordinateur...")
    subprocess.call("sudo reboot", shell=True)
    exit()

def optimiser_performances():
    print("Optimisation des performances...")
    subprocess.call("sudo sysctl vm.swappiness=10", shell=True)
    subprocess.call("sudo sysctl vm.dirty_ratio=5", shell=True)
    subprocess.call("sudo sysctl vm.dirty_background_ratio=10", shell=True)

def desactiver_demarrage():
    print("Désactivation des programmes au démarrage...")
    subprocess.call("sudo systemctl disable <nom_du_service>", shell=True)
   
def parametres_alimentation():
    print("Modification des paramètres d'alimentation...")
    subprocess.call("sudo cp /etc/default/grub /etc/default/grub.backup", shell=True)
    subprocess.call("sudo sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT=\"quiet splash\"/GRUB_CMDLINE_LINUX_DEFAULT=\"quiet splash acpi=off\"/' /etc/default/grub", shell=True)
    subprocess.call("sudo update-grub", shell=True)

def menu():
    while True:
        print("\nMenu:")
        print("1 - Nettoyage de disque")
        print("2 - Nettoyage des fichiers temporaires")
        print("3 - Nettoyage du cache DNS")
        print("4 - Nettoyage du cache ARP")
        print("5 - Vérification de l'intégrité des fichiers système")
        print("6 - Mise à jour système")
        print("7 - Redémarrer l'ordinateur")
        print("8 - Optimiser les performances")
        print("9 - Désactiver les programmes au démarrage")
        print("0 - Modifier les paramètres d'alimentation")

        choix = input("Entrez votre choix: ")

        if choix == "1":
            nettoyage_disque()
        elif choix == "2":
            nettoyage_temp()
        elif choix == "3":
            nettoyage_dns()
        elif choix == "4":
            nettoyage_arp()
        elif choix == "5":
            verification_systeme()
        elif choix == "6":
            mise_a_jour()
        elif choix == "7":
            redemarrer()
        elif choix.upper() == "8":
            optimiser_performances()
        elif choix.upper() == "9":
            desactiver_demarrage()
        elif choix.upper() == "0":
            parametres_alimentation()
        else:
            print("Choix invalide")

if __name__ == "__main__":
    menu()
