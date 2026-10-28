
import tkinter as tk
from datetime import date

window = tk.Tk()
window.title("Workshop Participant Greeting")
window.geometry("450x350")

instruction_label = tk.Label(
    window,
    text="Welcome to the Workshop!",
    font=("Arial", 16, "bold")
)
instruction_label.pack(pady=10)

name_label = tk.Label(
    window,
    text="Enter your name:"
)
name_label.pack()

name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=5)

output_text = tk.Text(window, height=6, width=40)
output_text.pack(pady=10)

def check_in():
    name = name_entry.get().strip()

    if name:
        message = (
            f"Hello, {name}!\n"
            "Welcome to our workshop.\n"
            f"Workshop Date: {date.today().strftime('%d-%m-%Y')}\n"
            "We hope you have a great learning experience!"
        )
    else:
        message = "Please enter your name before checking in."

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, message)

check_in_button = tk.Button(
    window,
    text="Check In",
    command=check_in
)
check_in_button.pack()

window.mainloop()
