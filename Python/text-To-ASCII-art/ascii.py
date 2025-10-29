# ASCII Art Text Converter with GUI and Font Selection
# pip install pyfiglet

import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
import pyfiglet

def convert_text():
    text = text_entry.get().strip()
    font = font_combo.get().strip()

    if not text:
        messagebox.showwarning("Input Required", "Please enter some text!")
        return

    try:
        art = pyfiglet.figlet_format(text, font=font if font else "standard")
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, art)
    except pyfiglet.FontNotFound:
        messagebox.showerror("Error", "Selected font not found! Using default font.")
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, pyfiglet.figlet_format(text))

# --- GUI Setup ---
root = tk.Tk()
root.title("ASCII Art Converter")
root.geometry("650x550")
root.resizable(False, False)

title_label = tk.Label(root, text="🎨 ASCII Art Text Converter", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Input Section
tk.Label(root, text="Enter Text:", font=("Arial", 11)).pack()
text_entry = tk.Entry(root, width=50, font=("Consolas", 11))
text_entry.pack(pady=5)

# Font Selection Dropdown
tk.Label(root, text="Choose Font:", font=("Arial", 11)).pack(pady=5)
available_fonts = sorted(["slant", "3-d", "bubble", "digital", "starwars", "banner", "block", "doom", "shadow", "standard"])
font_combo = ttk.Combobox(root, values=available_fonts, width=47, font=("Consolas", 10))
font_combo.set("standard")  # Default font
font_combo.pack(pady=5)

# Convert Button
convert_btn = tk.Button(root, text="Convert to ASCII Art", command=convert_text, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
convert_btn.pack(pady=10)

# Output Section
tk.Label(root, text="Generated ASCII Art:", font=("Arial", 11)).pack()
output_box = scrolledtext.ScrolledText(root, width=75, height=15, wrap=tk.WORD, font=("Courier", 10))
output_box.pack(pady=10)

# Run GUI
root.mainloop()
