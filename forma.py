# import tkinter as tk
# import tkinter.filedialog
#
# window = tk.Tk()  # Создаем новое окно
# window.geometry("600x640")  # Задаем окну размеры
# window.title(u"Primitive shapes")  # Задаем заголовок окна
#
# def add_new_shape_click():
#     button = tk.Button(window, text='Add', width=10, command=add_new_shape_click)
#     button.pack(side=tk.TOP)
#
#     textbox = tk.
#     textbox.pack(side=tk.TOP)
#     pass
#
# def tr():
#     print(2)
#
# for x in range(9):
#     button = tk.Button(window, text='Add', width=10, command=add_new_shape_click)
#     button.pack(side=tkinter.LEFT)
#
#
#
# # tkinter.filedialog.askdirectory()
#


# _list = tk.Checkbutton(window,text='Нажми', command=tr)
# _list.pack(side=tk.LEFT)
#
# # .. Весь остальной код, будем добавлять сюда
#
# window.mainloop()  # Отображаем окно

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

window = tk.Tk()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()


