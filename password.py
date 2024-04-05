import random
import string
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import pyperclip

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    length_str = length_entry.get()
    if length_str.isdigit():
        length = int(length_str)
        password = generate_password(length)
        password_label.config(text="Generated Password: " + password)
    else:
        messagebox.showerror("Error", "Please enter a valid integer for password length")

def copy_to_clipboard():
    password = password_label.cget("text")[18:]
    pyperclip.copy(password)
    messagebox.showinfo("Success", "Password copied to clipboard")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("300x150")  # Set window size

# Add a theme
style = ttk.Style()
style.theme_use("clam")  # Choose a theme (e.g., clam, default, alt, etc.)

# Set background color to dark brown
root.configure(bg="#edd1b0")

# Create widgets
length_label = tk.Label(root, text="Password Length:", bg="#edd1b0", fg="black")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack()

password_label = tk.Label(root, text="", bg="#edd1b0", fg="black")
password_label.pack()

copy_button = tk.Button(root, text="Copy Password", command=copy_to_clipboard)
copy_button.pack()

# Run the application
root.mainloop()