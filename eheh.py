# remove_bg_simple_gui.py
import os
import tkinter as tk
from tkinter import scrolledtext
from rembg import remove
from PIL import Image

# Folders
current_folder = os.path.dirname(os.path.abspath(__file__))
input_folder = current_folder
output_folder = os.path.join(current_folder, "output_images")
os.makedirs(output_folder, exist_ok=True)

def log(message):
    log_text.config(state='normal')
    log_text.insert(tk.END, message + '\n')
    log_text.yview(tk.END)
    log_text.config(state='disabled')

def remove_backgrounds():
    log("Starting background removal...")
    processed_count = 0
    failed_count = 0

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            try:
                with Image.open(input_path) as img:
                    result = remove(img)
                    result.save(output_path)
                log(f"Processed: {file_name}")
                processed_count += 1
            except Exception as e:
                log(f"Failed: {file_name} ({e})")
                failed_count += 1

    log(f"Done! Processed: {processed_count}, Failed: {failed_count}")

# GUI setup
root = tk.Tk()
root.title("Simple Background Remover")

tk.Button(root, text="Start Background Removal", command=remove_backgrounds, width=30, bg='lightgreen').pack(pady=10)
log_text = scrolledtext.ScrolledText(root, width=70, height=20, state='disabled')
log_text.pack(padx=10, pady=10)

root.mainloop()
