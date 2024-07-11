# Assighnment
#1. function to load key
from cryptography.fernet import Fernet

def load_key(key_file):
    """
    Load encryption key from a file.

    Args:
    - key_file (str): Path to the file containing the key.

    Returns:
    - Fernet object: Fernet encryption/decryption object initialized with the loaded key.
    """
    try:
        with open(key_file, "rb") as f:
            key = f.read()
            return Fernet(key)
    except FileNotFoundError:
        print(f"Key file '{key_file}' not found.")
        return None
    except Exception as e:
        print(f"Error loading key: {e}")
        return None


key_file = "secret.key"  
cipher_suite = load_key(key_file)

if cipher_suite:
    plaintext = b"Hello, this is a secret message."
    cipher_text = cipher_suite.encrypt(plaintext)
    print("Encrypted:", cipher_text)

    decrypted_text = cipher_suite.decrypt(cipher_text)
print("Decrypted:", decrypted_text.decode())

#2. encrypt data using loaded key
from cryptography.fernet import Fernet

def load_key(key_file):
    """
    Load encryption key from a file.

    Args:
    - key_file (str): Path to the file containing the key.

    Returns:
    - Fernet object: Fernet encryption/decryption object initialized with the loaded key.
    """
    try:
        with open(key_file, "rb") as f:
            key = f.read()
            return Fernet(key)
    except FileNotFoundError:
        print(f"Key file '{key_file}' not found.")
        return None
    except Exception as e:
        print(f"Error loading key: {e}")
        return None

def encrypt_data(data, cipher_suite):
    """
    Encrypt data using the provided Fernet encryption object.

    Args:
    - data (bytes): Data to encrypt.
    - cipher_suite (Fernet): Fernet encryption object initialized with the encryption key.

    Returns:
    - bytes: Encrypted data.
    """
    encrypted_data = cipher_suite.encrypt(data)
    return encrypted_data


key_file = "secret.key"  
cipher_suite = load_key(key_file)

if cipher_suite:
    plaintext = b"Hello, this is a secret message."
    encrypted_message = encrypt_data(plaintext, cipher_suite)
print("Encrypted:", encrypted_message)
#3. decrypt data using loaded key
from cryptography.fernet import Fernet

def load_key(key_file):
    """
    Load encryption key from a file.

    Args:
    - key_file (str): Path to the file containing the key.

    Returns:
    - Fernet object: Fernet encryption/decryption object initialized with the loaded key.
    """
    try:
        with open(key_file, "rb") as f:
            key = f.read()
            return Fernet(key)
    except FileNotFoundError:
        print(f"Key file '{key_file}' not found.")
        return None
    except Exception as e:
        print(f"Error loading key: {e}")
        return None

def encrypt_data(data, cipher_suite):
    """
    Encrypt data using the provided Fernet encryption object.

    Args:
    - data (bytes): Data to encrypt.
    - cipher_suite (Fernet): Fernet encryption object initialized with the encryption key.

    Returns:
    - bytes: Encrypted data.
    """
    encrypted_data = cipher_suite.encrypt(data)
    return encrypted_data

def decrypt_data(encrypted_data, cipher_suite):
    """
    Decrypt data using the provided Fernet encryption object.

    Args:
    - encrypted_data (bytes): Encrypted data to decrypt.
    - cipher_suite (Fernet): Fernet encryption object initialized with the decryption key.

    Returns:
    - bytes: Decrypted data.
    """
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data


key_file = "secret.key"  
cipher_suite = load_key(key_file)

if cipher_suite:
    plaintext = b"Hello, this is a secret message."
    encrypted_message = encrypt_data(plaintext, cipher_suite)
    print("Encrypted:", encrypted_message)

    decrypted_message = decrypt_data(encrypted_message, cipher_suite)
print("Decrypted:", decrypted_message.decode())

# 4. Recap on APIs in flask I.e post employee
# 5. Install Postman and create an acc with postman