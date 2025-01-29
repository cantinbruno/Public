import requests
import threading
from time import time
print_lock = threading.Lock()

def interpreter_code_statut(code):
    if code == 200:
        return "OK - La requête a réussi."
    elif code == 404:
        return "Not Found - La ressource demandée n'a pas été trouvée."
    elif code == 500:
        return "Internal Server Error - Le serveur a rencontré une condition inattendue."
     elif code == 403:
        return "Interdiction à un client d'accéder à l'URL"
    else:
        return "Code de statut non géré spécifiquement par ce script."

def envoyer_requete(url):
    try:
        response = requests.get(url)
        interpretation = interpreter_code_statut(response.status_code)
        with print_lock:
            print(f"Réponse {response.status_code}: {interpretation}\n")
    except Exception as e:
        with print_lock:
            print(f"Erreur lors de l'envoi de la requête: {e}\n")

def test_de_charge(url, nombre_de_requetes, nombre_de_threads):
    threads = []
    start_time = time()
    for i in range(nombre_de_requetes):
        t = threading.Thread(target=envoyer_requete, args=(url,))
        t.start()
        threads.append(t)
        if len(threads) >= nombre_de_threads:
            for t in threads:
                t.join()
            threads = []
    for t in threads:
        t.join()
    total_time = time() - start_time
    print(f"Test terminé en {total_time} secondes")

if __name__ == "__main__":
    url = input("Veuillez entrer l'URL : ")
    nombre_de_requetes = int(input("Veuillez entrer le nombre total de requêtes à envoyer : "))
    nombre_de_threads = int(input("Veuillez entrer le nombre de threads (utilisateurs simultanés) : "))
    test_de_charge(url, nombre_de_requetes, nombre_de_threads)
