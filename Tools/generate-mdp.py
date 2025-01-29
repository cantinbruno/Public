import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

new_password = generate_password(12)
print(f"Votre nouveau mot de passe est: {new_password}")
