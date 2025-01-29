import os
import subprocess

def nettoyage_disque():
    print("Execution du nettoyage de disque...")
    subprocess.call("cleanmgr /sagerun", shell=True)

def nettoyage_temp():
    print("Suppression des fichiers temporaires...")
    subprocess.call("del /f /s /q %temp%\*", shell=True)
    subprocess.call("del /f /s /q C:\\Windows\\Temp\\*", shell=True)

def nettoyage_dns():
    print("Nettoyage du cache DNS...")
    subprocess.call("ipconfig /flushdns", shell=True)

def nettoyage_arp():
    print("Nettoyage du cache ARP...")
    subprocess.call("arp -d *", shell=True)

def verification_systeme():
    print("Verification de l'integrite des fichiers systeme...")
    subprocess.call("sfc /scannow", shell=True)

def mise_a_jour():
    print("Mise a jour du systeme...")
    subprocess.call("wuauclt /updatenow", shell=True)

def redemarrer():
    print("Redemarrage de l'ordinateur...")
    subprocess.call("shutdown /r /t 0", shell=True)
    exit()

def optimiser_performances():
    print("Optimisation des performances...")
    print("Desactivation des effets visuels...")
    subprocess.call("SystemPropertiesPerformance", shell=True)

def desactiver_demarrage():
    print("Desactivation des programmes au demarrage...")
    subprocess.call("msconfig", shell=True)

def parametres_alimentation():
    print("Modification des parametres d'alimentation...")
    subprocess.call("powercfg.cpl", shell=True)

def menu():
    while True:
        print("\nMenu:")
        print("1 - Nettoyage de disque")
        print("2 - Nettoyage des fichiers temporaires")
        print("3 - Nettoyage du cache DNS")
        print("4 - Nettoyage du cache ARP")
        print("5 - Verification de l'integrite des fichiers systeme")
        print("6 - Mise a jour système")
        print("7 - Redemarrer l'ordinateur")
        print("8 - Optimiser les performances")
        print("9 - Desactiver les programmes au demarrage")
        print("0 - Modifier les parametres d'alimentation")

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
