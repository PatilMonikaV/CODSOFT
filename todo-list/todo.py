import tkinter as tk

class ToDoList(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.tasks = []

        self.task_list = tk.Listbox(self)
        self.task_list.pack()

        self.add_task_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.delete_task_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

    def add_task(self):
        task = tk.Entry(self)
        task.pack()

        self.tasks.append(task)

    def delete_task(self):
        task = self.task_list.get(tk.ANCHOR)
        self.tasks.remove(task)
        self.task_list.delete(tk.ANCHOR)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List")

    todo_list = ToDoList(root)
    todo_list.pack()

    root.mainloop()