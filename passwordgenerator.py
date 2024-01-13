import tkinter as tk
from tkinter import messagebox
import random

class PasswordGeneratorApp:
    def _init_(self, master):
        self.master = master
        self.master.geometry('400x400')
        self.master.title("Password Generator")

        # Labels
        labels = {'n_letters': 'letters:', 'n_symbols': 'Symbols:', 'n_numbers': 'Digits:'}
        for key, value in labels.items():
            label = tk.Label(text=value)
            label.place(x=120, y=140 + 40 * list(labels.keys()).index(key), width=50)

        # StringVars
        self.letters_var = tk.StringVar()
        self.symbols_var = tk.StringVar()
        self.numbers_var = tk.StringVar()

        # Entries
        self.letters_entry = tk.Entry(width=15, textvariable=self.letters_var)
        self.letters_entry.place(x=175, y=140)
        self.symbols_entry = tk.Entry(width=15, textvariable=self.symbols_var)
        self.symbols_entry.place(x=175, y=180)
        self.numbers_entry = tk.Entry(width=15, textvariable=self.numbers_var)
        self.numbers_entry.place(x=175, y=220)
        self.password_entry = tk.Entry(width=30)
        self.password_entry.place(x=130, y=70, height=40)

        # Button
        generate = tk.Button(self.master, text='GENERATE', bg='red', command=self.generate_pass)
        generate.place(x=175, y=350, height=25, width=92)

    def generate_pass(self):
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '@#$&'

        try:
            n_letters = int(self.letters_var.get())
            n_symbols = int(self.symbols_var.get())
            n_numbers = int(self.numbers_var.get())
        except ValueError:
            messagebox.showerror(title='ATTENTION', message='Please enter valid numbers.')
            return

        if n_letters < 0 or n_symbols < 0 or n_numbers < 0:
            messagebox.showerror(title='ATTENTION', message='Please enter positive numbers.')
            return

        all_characters = letters + symbols + numbers

        password_list = [random.choice(all_characters) for _ in range(n_letters + n_symbols + n_numbers)]
        random.shuffle(password_list)

        password = ''.join(password_list)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        messagebox.showinfo(title='CONFIRMATION', message='Password generated successfully!!')

if _name_ == "_main_":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
