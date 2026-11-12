import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title("Letter Editor")
window.geometry("700x500")
def open_letter():
    filename = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if filename:
        with open(filename, "r") as file:
            text.delete("1.0", tk.END)
            text.insert("1.0", file.read())

def save_letter():
    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if filename:
        with open(filename, "w") as file:
            file.write(text.get("1.0", tk.END))

text = tk.Text(window, width=70, height=25)
text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

open_button = tk.Button(window, text="Open Letter", command=open_letter)
open_button.grid(row=1, column=0, padx=10, pady=10)

save_button = tk.Button(window, text="Save As", command=save_letter)
save_button.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()