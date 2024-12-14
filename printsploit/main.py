import hashlib
import os
import subprocess
import tkinter as tk
from tkinter import messagebox

SECRET = "my_secret_key_2024"

def generate_key(username: str) -> str:
    data = f"{username}:{SECRET}".encode()
    return hashlib.sha256(data).hexdigest()

def run_command_with_dylib():
    try:
        dylib_path = os.path.abspath("./printsploit.dylib")
        roblox_path = "/Applications/Roblox.app/Contents/MacOS/RobloxPlayer"

        if os.path.exists(dylib_path) and os.path.exists(roblox_path):
            cmd = f'DYLD_INSERT_LIBRARIES="{dylib_path}" "{roblox_path}"'
            subprocess.run(cmd, shell=True)
            messagebox.showinfo("Success", "DYLD injection executed successfully.")
        else:
            messagebox.showerror("Error", "Required files not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def validate_key():
    entered_key = key_entry.get()
    if entered_key == valid_key:
        messagebox.showinfo("Access Granted", "Key is valid. Proceeding to execution.")
        show_execution_options()
    else:
        messagebox.showerror("Access Denied", "Invalid key. Please try again.")

def generate_key_screen():
    username = username_entry.get().strip()
    global valid_key
    valid_key = generate_key(username)

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Your key is:", font=("Arial", 16), bg="#2e2e2e", fg="white").pack(pady=10)
    key_display = tk.Entry(root, font=("Arial", 14), width=50, bg="#1e1e1e", fg="white")
    key_display.insert(0, valid_key)
    key_display.pack(pady=10)
    key_display.configure(state="readonly")

    tk.Button(root, text="Continue", command=validate_key_screen, font=("Arial", 14), bg="#5cb85c", fg="white", width=20).pack(pady=20)

def validate_key_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Enter your key:", font=("Arial", 16), bg="#2e2e2e", fg="white").pack(pady=10)
    global key_entry
    key_entry = tk.Entry(root, font=("Arial", 14), width=50, bg="#1e1e1e", fg="white")
    key_entry.pack(pady=10)

    tk.Button(root, text="Submit", command=validate_key, font=("Arial", 14), bg="#5cb85c", fg="white", width=20).pack(pady=20)

def show_execution_options():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Execution Options", font=("Arial", 16), bg="#2e2e2e", fg="white").pack(pady=10)
    tk.Button(root, text="Run with DYLD Injection", command=run_command_with_dylib, font=("Arial", 14), bg="#0275d8", fg="white", width=30).pack(pady=10)

root = tk.Tk()
root.title("Key System")
root.geometry("600x400")
root.configure(bg="#2e2e2e")

tk.Label(root, text="Enter your username:", font=("Arial", 16), bg="#2e2e2e", fg="white").pack(pady=10)
username_entry = tk.Entry(root, font=("Arial", 14), width=50, bg="#1e1e1e", fg="white")
username_entry.pack(pady=10)
tk.Button(root, text="Generate Key", command=generate_key_screen, font=("Arial", 14), bg="#5cb85c", fg="white", width=20).pack(pady=20)

root.mainloop()
