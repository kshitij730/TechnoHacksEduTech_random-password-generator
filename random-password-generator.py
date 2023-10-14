import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string
from ttkthemes import ThemedTk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_callback():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length should be a positive integer.")
        else:
            password = generate_password(length)
            password_display.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

root = ThemedTk(theme="radiance")  # Create ThemedTk window with the "radiance" theme
root.title("Random Password Generator")
root.geometry("400x200")

frame = ttk.Frame(root)
frame.pack(pady=20)

length_label = ttk.Label(frame, text="Enter Password Length:")
length_label.grid(row=0, column=0, padx=10)

length_entry = ttk.Entry(frame)
length_entry.grid(row=0, column=1, padx=10)

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password_callback)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

password_display = ttk.Label(root, text="")
password_display.pack(pady=10)

root.mainloop()
