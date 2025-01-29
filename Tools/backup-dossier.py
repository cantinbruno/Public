import shutil
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def backup_files(source_folder, backup_folder):
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    for file_name in os.listdir(source_folder):
        full_file_name = os.path.join(source_folder, file_name)
        if os.path.isfile(full_file_name):
            destination_file = os.path.join(backup_folder, file_name)
            try:
                shutil.copy2(full_file_name, destination_file)
                logging.info(f"Fichier sauvegardé : {destination_file}")
            except Exception as e:
                logging.error(f"Erreur lors de la copie du fichier {file_name}: {e}")

source_path = input("Entrez le chemin du dossier source : ")
destination_path = input("Entrez le chemin du dossier de sauvegarde : ")

backup_files(source_path, destination_path)
