import tkinter as tk
from tkinter import filedialog
import os


def view_table():
    file = filedialog.askopenfilename()
    try:
        file_path = os.path.basename(file)
        with open(file_path, 'r') as f:
            content = f.read()
            print(content)
    except(AttributeError, FileNotFoundError):
        print("Some error occurred")


root = tk.Tk()
root.title("Trading Data App")

menubar = tk.Menu()
root.config(menu=menubar)

File = tk.Menu(menubar)
menubar.add_cascade(label="App")
menubar.add_cascade(label="File", menu=File)

File.add_command(label="Load")
File.add_command(label="Clear")
File.add_command(label="View Tables", command=view_table)
File.add_command(label="Create Tables")
root.mainloop()
