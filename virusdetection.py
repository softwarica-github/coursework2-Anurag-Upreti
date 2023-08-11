import tkinter as tk
from tkinter import filedialog
import hashlib
import os

def calculate_hash(file_path, block_size=65536):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def store_hash(file_path, hash_value):
    with open('hashes.txt', 'a') as f:
        f.write(f"{file_path}: {hash_value}\n")

def check_hash(file_path, stored_hash):
    current_hash = calculate_hash(file_path)
    return current_hash == stored_hash

def open_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=(("All files", "*.*"),))
    if file_path:
        current_hash = calculate_hash(file_path)
        store_hash(file_path, current_hash)
        result_label.config(text=f"File Hash: {current_hash}")

def check_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=(("All files", "*.*"),))
    if file_path:
        with open('hashes.txt', 'r') as f:
            for line in f:
                stored_path, stored_hash = line.strip().split(': ')
                if stored_path == file_path and check_hash(file_path, stored_hash):
                    result_label.config(text="File integrity verified!", fg="green")
                    return
        result_label.config(text="File integrity check failed", fg="red")

# Create the main window
root = tk.Tk()
root.title("Virus Detection and File Integrity Check")
root.geometry("800x400")
root.configure(bg="lightblue")
root.resizable(False, False)

# Create and place widgets
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=10)

check_button = tk.Button(root, text="Check File Integrity", command=check_file)
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Start the main loop
root.mainloop()
