import json
import os
import base64

# Features - Command Line Application
'''
Encryption, Decryption, Uninterrupted Flow
Site Name, URL, Password, File Handling, JSON (Javascript Object Notation)
'''

# Todos
'''
Customly Get list of similiar keys in the dictionary
It should show list of items similiar to the input demand
It should verify before decrypting password
'''

class AddNewPassword:
    # New Password with fields, name, url, password
    def __init__(self, name, url, password):
        self.name = name
        self.url = url
        self.password = password

    def __str__(self):
        return f"Password Saved for '{self.name}', Location at '{self.url}', with encryption '{self.password}'"

    def __repr__(self):
        return self.__str__()

    def Encrypt(self):
        t1 = "2v8c6tsdag8"
        t2 = "br92crt383r"
        encoded = base64.b64encode(self.password.encode()).decode()
        return f"{t1}{encoded}{t2}"

    def Decrypt(self):
        t1 = "2v8c6tsdag8"
        t2 = "br92crt383r"

        if self.password.startswith(t1) and self.password.endswith(t2):
            encoded = self.password[len(t1):-len(t2)]
            try:
                decoded = base64.b64decode(encoded.encode()).decode()
                return decoded
            except Exception as e:
                return "Decryption Failed"
        return "Decryption Failed"

filename = "passwords.json"
dictionary = {}

def save_passwords():
    try:
        with open(filename, "w") as f:
            json.dump(dictionary, f)
    except Exception as e:
        print("Error saving passwords:", e)

def load_passwords():
    try:
        global dictionary
        if os.path.exists(filename):
            with open(filename, "r") as f:
                dictionary = json.load(f)
    except Exception as e:
        print("Error loading passwords:", e)

def addnewpassword():
    try:
        n = input("Enter Name: ").strip()
        name = n.lower()
        url = input("Enter Url: ").strip()
        password = input("Enter Password: ").strip()

        if not name or not password:
            print("Name and password cannot be empty.")
            return

        encrypted = AddNewPassword(name, url, password).Encrypt()
        dictionary[name] = encrypted
        print("Encrypted Password:", encrypted)
        save_passwords()
    except Exception as e:
        print("Error adding new password:", e)

def show(name):
    try:
        if name not in dictionary:
            return f"No password found for '{name}'"

        encrypted_password = dictionary[name]
        obj = AddNewPassword(name, "dummy_url", encrypted_password)
        decrypted = obj.Decrypt()
        return f"Decrypted Password for '{name}': {decrypted}"
    except Exception as e:
        return f"Error: {e}"

try:
    load_passwords()
except Exception as e:
    print("Error during startup:", e)

while True:
    try:
        print("1. Add\n2. Show\n")
        choice = input("--> ").strip()

        if not choice:
            print("Input cannot be empty.")
            continue

        user = int(choice)

        if user == 1:
            addnewpassword()
        elif user == 2:
            n = input("Enter Name: ").strip()
            name = n.lower()
            if name:
                print(show(name))
            else:
                print("Name cannot be empty.")
        else:
            print("Invalid Input!")
    except ValueError:
        print("Please enter a number (1 or 2).")
    except Exception as e:
        print("Error:", e)
