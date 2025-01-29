import os
import subprocess
import sys

def check_superuser():
    if os.geteuid() != 0:
        sys.exit("Ce script doit être exécuté avec des privilèges de superutilisateur.")

def crack_passwords():
    passwd_file = "/etc/passwd"
    shadow_file = "/etc/shadow"
    output_file = "/tmp/unshadowed.txt"
    
    try:
        with open(output_file, 'w') as outfile:
            subprocess.run(["unshadow", passwd_file, shadow_file], stdout=outfile)
        print(f"Le fichier unshadowed a été créé à: {output_file}")
    except Exception as e:
        sys.exit(f"Erreur lors de la création du fichier unshadowed: {str(e)}")
    
    if not os.path.exists(output_file):
        sys.exit(f"Le fichier unshadowed n'existe pas : {output_file}")
    
    subprocess.run(["john", output_file])
    subprocess.run(["john", "--show", output_file])

if __name__ == "__main__":
    check_superuser()
    crack_passwords()
