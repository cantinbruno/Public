from instapy import InstaPy
import random
import time

# Instancier le bot InstaPy
session = InstaPy(username='ton_nom_utilisateur', password='ton_mot_de_passe')

# Se connecter à Instagram
session.login()

# Obtenir une liste de 100 utilisateurs au hasard qui ne sont pas abonnés
non_followers = session.pick_nonfollowers_randomly(quantity=100)

# Suivre chaque utilisateur de la liste non_followers
for user in non_followers:
    session.follow(user)
    time.sleep(1)  # Pause de 1 seconde pour éviter d'être bloqué par Instagram

# Attendre 5 minutes
time.sleep(300)

# Unfollow chaque utilisateur de la liste non_followers
for user in non_followers:
    session.unfollow(user)
    time.sleep(1)  # Pause de 1 seconde pour éviter d'être bloqué par Instagram

# Se déconnecter de Instagram
session.end()
