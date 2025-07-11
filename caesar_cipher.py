import tkinter as tk
from tkinter import ttk
import string

ALPHABET = string.ascii_lowercase

def shift_char(char, shift):
    return ALPHABET[(ALPHABET.index(char) + shift) % 26] if char in ALPHABET else char

def caesar_cipher(text, shift, mode):
    shift = shift if mode == "Encrypt" else -shift
    return ''.join(shift_char(c, shift) for c in text.lower())

def on_submit():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_var.get()) % 26
    except ValueError:
        result_var.set("❌ Shift must be a number.")
        return

    mode = mode_var.get()
    result = caesar_cipher(text, shift, mode)
    result_var.set(result)

# === GUI Setup ===
root = tk.Tk()
root.title("🗝️ Caesar Cipher App")
root.geometry("400x350")
root.resizable(False, False)

# === Input ===
ttk.Label(root, text="Enter text:").pack(pady=5)
input_text = tk.Text(root, height=4, width=40)
input_text.pack()

ttk.Label(root, text="Shift (number):").pack(pady=5)
shift_var = tk.StringVar()
ttk.Entry(root, textvariable=shift_var, width=10).pack()

ttk.Label(root, text="Choose mode:").pack(pady=5)
mode_var = tk.StringVar(value="Encrypt")
ttk.Combobox(root, textvariable=mode_var, values=["Encrypt", "Decrypt"], state="readonly").pack()

# === Submit ===
ttk.Button(root, text="Submit", command=on_submit).pack(pady=15)

# === Result ===
ttk.Label(root, text="Result:").pack()
result_var = tk.StringVar()
ttk.Label(root, textvariable=result_var, wraplength=350).pack()

root.mainloop()
