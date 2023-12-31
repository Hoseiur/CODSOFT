import tkinter as tk
from tkinter import messagebox

class TodoListApp(tk.Tk):
    def _init_(self):
        super()._init_()

        self.title("TO DO LIST")
        self.geometry('400x500')

        self.heading = tk.Label(self, text="TO DO LIST", font=("Rangile", 24, 'bold'), fg='red')
        self.heading.place(x=115, y=0)

        self.task_manager = TaskManager(self)

        self.show_list()

    def show_list(self):
        self.task_manager.load_tasks()
        self.task_manager.display_tasks()

class TaskManager:
    def _init_(self, master):
        self.master = master

        # Frame
        self.frame = tk.Frame(self.master, height=250, width=300, highlightbackground="black", highlightthickness=3)
        self.frame.place(x=50, y=50)

        self.tasklist = tk.Listbox(self.frame, font=('times new roman', 12, 'bold'), fg='white', bg='#6F8FAF', selectmode=tk.EXTENDED)
        self.tasklist.place(x=3, y=2, height=260, width=290)

        self.scrollbar = tk.Scrollbar(self.master, command=self.tasklist.yview, width=12)
        self.scrollbar.place(x=336, y=54, height=240)
        self.tasklist.config(yscrollcommand=self.scrollbar.set)

        self.getdata = tk.Entry(self.master, width=45, highlightbackground='black', highlightthickness=1)
        self.getdata.place(x=55, y=330, height=25)

        # Buttons
        buttons = [("ADD", self.add_data), ("UPDATE", self.update),
                   ("DELETE", self.delete), ("DONE", self.done)]

        for i, (text, command) in enumerate(buttons, start=1):
            button = tk.Button(self.master, text=text, bg='cyan', width=15, command=command)
            button.place(x=65 if i % 2 != 0 else 220, y=380 + (i - 1) // 2 * 50, height=30)

    def load_tasks(self, filename="khushi.txt"):
        try:
            with open(filename, 'r') as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self, filename="khushi.txt"):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def display_tasks(self):
        self.tasklist.delete(0, tk.END)
        for task in self.tasks:
            self.tasklist.insert(tk.END, task)

    def add_data(self):
        task = self.getdata.get()
        self.tasks.append(task)
        self.getdata.delete(0, tk.END)
        self.display_tasks()

    def update(self):
        selected_indices = self.tasklist.curselection()
        for index in selected_indices:
            task = self.getdata.get()
            self.tasks[index] = task
        self.getdata.delete(0, tk.END)
        self.display_tasks()

    def delete(self):
        selected_indices = self.tasklist.curselection()
        for index in reversed(selected_indices):
            del self.tasks[index]
        self.display_tasks()

    def done(self):
        selected_indices = self.tasklist.curselection()
        for index in selected_indices:
            self.tasks[index] += " ✔"
        self.display_tasks()
        self.save_tasks()
        messagebox.showinfo(title='COMPLETION', message='You completed the task(s) successfully !!')

if __name__ == "__main__":
    app = TodoListApp()
    app.mainloop()