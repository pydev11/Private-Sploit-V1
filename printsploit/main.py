import hashlib
import os
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

SECRET = "my_secret_key_2024"

def generate_key(username: str) -> str:
    data = f"{username}:{SECRET}".encode()
    return hashlib.sha256(data).hexdigest()

def show_log_ui(command_output: str, error_logs: str):
    log_window = tk.Toplevel()
    log_window.title("Execution Logs and Settings")
    log_window.geometry("600x400")

    notebook = ttk.Notebook(log_window)
    notebook.pack(expand=True, fill="both")

    logs_frame = tk.Frame(notebook, bg="#1e1e1e")
    notebook.add(logs_frame, text="Logs")

    logs_text = tk.Text(logs_frame, font=("Courier", 12), bg="#1e1e1e", fg="white", wrap="word")
    logs_text.insert("end", command_output)
    logs_text.pack(expand=True, fill="both", padx=10, pady=10)

    errors_frame = tk.Frame(notebook, bg="#1e1e1e")
    notebook.add(errors_frame, text="Errors")

    errors_text = tk.Text(errors_frame, font=("Courier", 12), bg="#1e1e1e", fg="red", wrap="word")
    errors_text.insert("end", error_logs)
    errors_text.pack(expand=True, fill="both", padx=10, pady=10)

    settings_frame = tk.Frame(notebook, bg="#1e1e1e")
    notebook.add(settings_frame, text="Settings")

    tk.Label(settings_frame, text="DYLIB Path:", font=("Arial", 12), bg="#1e1e1e", fg="white").pack(pady=5, anchor="w", padx=10)
    dylib_entry = tk.Entry(settings_frame, font=("Arial", 12), width=50, bg="#282c34", fg="white")
    dylib_entry.insert(0, os.path.abspath("./printsploit.dylib"))
    dylib_entry.pack(pady=5, padx=10)

    tk.Label(settings_frame, text="Target App Path:", font=("Arial", 12), bg="#1e1e1e", fg="white").pack(pady=5, anchor="w", padx=10)
    target_app_entry = tk.Entry(settings_frame, font=("Arial", 12), width=50, bg="#282c34", fg="white")
    target_app_entry.insert(0, "/Applications/Roblox.app/Contents/MacOS/RobloxPlayer")
    target_app_entry.pack(pady=5, padx=10)

    tk.Button(settings_frame, text="Save Settings", font=("Arial", 12), bg="#007acc", fg="white",
              command=lambda: save_settings(dylib_entry.get(), target_app_entry.get())).pack(pady=20)

def save_settings(dylib_path, target_app_path):
    with open("settings.txt", "w") as settings_file:
        settings_file.write(f"DYLIB={dylib_path}\n")
        settings_file.write(f"TARGET_APP={target_app_path}\n")
    messagebox.showinfo("Settings", "Settings saved successfully!")

def run_command_with_dylib():
    try:
        dylib_path = os.path.abspath("./printsploit.dylib")
        roblox_path = "/Applications/Roblox.app/Contents/MacOS/RobloxPlayer"

        if os.path.exists(dylib_path) and os.path.exists(roblox_path):
            cmd = f'DYLD_INSERT_LIBRARIES="{dylib_path}" "{roblox_path}"'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

            command_output = result.stdout or "No output."
            error_logs = result.stderr or "No errors."

            show_log_ui(command_output, error_logs)
        else:
            messagebox.showerror("Error", "Required files not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def validate_key():
    entered_key = key_entry.get()
    if entered_key == valid_key:
        messagebox.showinfo("Access Granted", "Key is valid. Proceeding with execution.")
        run_command_with_dylib()
    else:
        messagebox.showerror("Access Denied", "Invalid key. Please try again.")

def generate_key_screen():
    username = username_entry.get().strip()
    global valid_key
    valid_key = generate_key(username)

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Your key is:", font=("Arial", 14), bg="#1e1e1e", fg="white").pack(pady=10)
    key_display = tk.Entry(root, font=("Arial", 12), width=50, bg="#282c34", fg="white")
    key_display.insert(0, valid_key)
    key_display.pack(pady=10)
    key_display.configure(state="readonly")
    
    tk.Button(root, text="Continue", command=validate_key_screen, font=("Arial", 12), bg="#007acc", fg="white").pack(pady=20)

def validate_key_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Enter your key:", font=("Arial", 14), bg="#1e1e1e", fg="white").pack(pady=10)
    global key_entry
    key_entry = tk.Entry(root, font=("Arial", 12), width=50, bg="#282c34", fg="white")
    key_entry.pack(pady=10)

    tk.Button(root, text="Submit", command=validate_key, font=("Arial", 12), bg="#007acc", fg="white").pack(pady=20)

root = tk.Tk()
root.title("Key System")
root.geometry("500x300")
root.configure(bg="#1e1e1e")

tk.Label(root, text="Enter your username:", font=("Arial", 14), bg="#1e1e1e", fg="white").pack(pady=10)
username_entry = tk.Entry(root, font=("Arial", 12), width=50, bg="#282c34", fg="white")
username_entry.pack(pady=10)
tk.Button(root, text="Generate Key", command=generate_key_screen, font=("Arial", 12), bg="#007acc", fg="white").pack(pady=20)

root.mainloop()
