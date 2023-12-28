import tkinter as tk
from tkinter import messagebox
import random

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry('400x400')
        self.master.title("Password Generator")

        self.create_label_entry("letters:", 140)
        self.create_label_entry("Symbols:", 180)
        self.create_label_entry("Digits:", 220)

        self.password_entry = tk.Entry(width=30)
        self.password_entry.place(x=130, y=70, height=40)

        tk.Button(self.master, text='GENERATE', bg='green', command=self.generate_pass).place(x=175, y=350, height=25, width=92)

    def create_label_entry(self, label_text, y_position):
        tk.Label(text=label_text).place(x=120, y=y_position, width=50)
        entry = tk.Entry(width=15)
        entry.place(x=175, y=y_position)
        setattr(self, f"{label_text.lower()}_entry", entry)

    def generate_pass(self):
        try:
            n_letters, n_symbols, n_numbers = map(int, [self.letters_entry.get(), self.symbols_entry.get(), self.numbers_entry.get()])
        except ValueError:
            messagebox.showerror(title='ATTENTION', message='Please enter valid numbers.')
            return

        if any(num < 0 for num in [n_letters, n_symbols, n_numbers]):
            messagebox.showerror(title='ATTENTION', message='Please enter positive numbers.')
            return

        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        symbols = '@#$&'
        numbers = '0123456789'

        password_list = [random.choice(letters) for _ in range(n_letters)]
        password_list += [random.choice(symbols) for _ in range(n_symbols)]
        password_list += [random.choice(numbers) for _ in range(n_numbers)]

        random.shuffle(password_list)

        password = ''.join(password_list)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        messagebox.showinfo(title='CONFIRMATION', message='Password generated successfully!!')

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
