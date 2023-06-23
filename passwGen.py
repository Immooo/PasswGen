import string
import random
import tkinter as tk
from tkinter import messagebox, ttk

def generate_password(length=8, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special_chars=True):
    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_numbers:
        characters += string.digits

    if use_special_chars:
        characters += string.punctuation

    if len(characters) == 0:
        raise ValueError("Vous devez inclure au moins un type de caractère pour générer un mot de passe.")

    password = "".join(random.choice(characters) for _ in range(length))

    return password

def generate():
    try:
        length = int(entry_length.get())
        use_uppercase = bool(var_uppercase.get())
        use_lowercase = bool(var_lowercase.get())
        use_numbers = bool(var_numbers.get())
        use_special_chars = bool(var_special_chars.get())
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Erreur", "La longueur doit être un nombre entier.")

root = tk.Tk()
root.title("Générateur de mot de passe")

mainframe = ttk.Frame(root, padding="30 15")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_length = ttk.Label(mainframe, text="Longueur du mot de passe :")
label_length.grid(column=0, row=0, sticky=tk.W)

entry_length = ttk.Entry(mainframe)
entry_length.grid(column=1, row=0, sticky=(tk.W, tk.E))

var_uppercase = tk.IntVar()
check_uppercase = ttk.Checkbutton(mainframe, text="Inclure des lettres majuscules", variable=var_uppercase)
check_uppercase.grid(column=0, row=1, sticky=tk.W)

var_lowercase = tk.IntVar()
check_lowercase = ttk.Checkbutton(mainframe, text="Inclure des lettres minuscules", variable=var_lowercase)
check_lowercase.grid(column=0, row=2, sticky=tk.W)

var_numbers = tk.IntVar()
check_numbers = ttk.Checkbutton(mainframe, text="Inclure des chiffres", variable=var_numbers)
check_numbers.grid(column=0, row=3, sticky=tk.W)

var_special_chars = tk.IntVar()
check_special_chars = ttk.Checkbutton(mainframe, text="Inclure des caractères spéciaux", variable=var_special_chars)
check_special_chars.grid(column=0, row=4, sticky=tk.W)

button_generate = ttk.Button(mainframe, text="Générer", command=generate)
button_generate.grid(column=1, row=5)

label_password = ttk.Label(mainframe, text="Mot de passe généré :")
label_password.grid(column=0, row=6, sticky=tk.W)

entry_password = ttk.Entry(mainframe)
entry_password.grid(column=1, row=6, sticky=(tk.W, tk.E))

root.mainloop()
