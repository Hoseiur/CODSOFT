from tkinter import *
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        master.geometry("400x400")
        master.config(bg='white')

        self.create_widgets()

    def create_widgets(self):
        # Label
        self.name = Label(self.master, text="Calculator", fg='black', font=('Serif', 20, 'bold'), bg='white')
        self.name.grid(row=0, column=1, pady=10)

        # Entry
        self.calsi = Entry(self.master)
        self.calsi.grid(row=1, column=0, columnspan=4, pady=10)

        # Buttons
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 1), ('C', 5, 0), ('=', 5, 2), ('+', 5, 3)
        ]

        for (text, row, column) in buttons:
            button = Button(self.master, text=text, font=('Serif', 12, 'bold'), command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5, ipadx=10, ipady=10)

    def button_click(self, value):
        if value == '=':
            self.calculate()
        elif value == 'C':
            self.clear_entry()
        else:
            self.calsi.insert(END, value)

    def clear_entry(self):
        self.calsi.delete(0, END)

    def calculate(self):
        try:
            expression = self.calsi.get()
            result = eval(expression)
            self.clear_entry()
            self.calsi.insert(0, result)
        except ZeroDivisionError:
            messagebox.showerror(title='ATTENTION', message='Division by zero is not possible')
        except Exception as e:
            messagebox.showerror(title='ATTENTION', message=f'Error: {e}')

if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()
