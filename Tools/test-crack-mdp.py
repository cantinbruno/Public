import hashlib
import itertools
import string
import time

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force_attack(hash_to_crack, max_length=6):
    characters = string.ascii_lowercase + string.digits
    for password_length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=password_length):
            guess = ''.join(guess)
            if hash_password(guess) == hash_to_crack:
                return guess
    return None

def test_password_cracking():
    password = input("Please enter a password to hash and crack: ")
    hashed_password = hash_password(password)
    print("Hashed Password:", hashed_password)
    
    start_time = time.time()  
    cracked_password = brute_force_attack(hashed_password, max_length=6)
    end_time = time.time()
    elapsed_time = end_time - start_time  
    
    if cracked_password:
        print("Password cracked:", cracked_password)
        print(f"Time taken to crack: {elapsed_time:.2f} seconds")
    else:
        print("Failed to crack the password.")
        print(f"Time taken: {elapsed_time:.2f} seconds")

test_password_cracking()

