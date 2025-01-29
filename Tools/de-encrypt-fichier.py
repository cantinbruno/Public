from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from os import urandom, path
import base64

def derive_key(password: bytes, salt: bytes) -> bytes:
    """Generate a cryptographic key using PBKDF2HMAC"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password)

def encrypt(file_path: str, password: bytes) -> str:
    """Encrypt the file and save salt, iv, and ciphertext in a single file"""
    salt = urandom(16)  
    key = derive_key(password, salt)
    
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    iv = urandom(16)  
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as file:
        file.write(base64.b64encode(salt + iv + ciphertext))  # Store salt, iv, and ciphertext together
    return encrypted_file_path

def decrypt(encrypted_file_path: str, password: bytes) -> None:
    """Decrypt the file using the stored salt, iv from the encrypted file"""
    with open(encrypted_file_path, 'rb') as file:
        data = base64.b64decode(file.read())
    salt = data[:16]  
    iv = data[16:32]  
    ciphertext = data[32:]  
    key = derive_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    try:
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
        
        decrypted_file_path = path.splitext(encrypted_file_path)[0]
        with open(decrypted_file_path, 'wb') as file:
            file.write(plaintext)
        print(f"File decrypted successfully. Decrypted file saved as: {decrypted_file_path}")
    except Exception as e:
        print(f"Error during decryption: {e}")

def main():
    choice = input("Do you want to encrypt or decrypt a file? (e/d): ").lower()
    password = input("Enter your password: ").encode()
    
    if choice == 'e':
        file_path = input("Enter the path of the file to encrypt: ")
        encrypted_file_path = encrypt(file_path, password)
        print(f"File encrypted successfully. Encrypted file saved as: {encrypted_file_path}")
    elif choice == 'd':
        encrypted_file_path = input("Enter the path of the encrypted file: ")
        decrypt(encrypted_file_path, password)
    else:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
