import tkinter as tk
from tkinter import filedialog, messagebox
import markdown

# --- Hover effects for buttons ---
def on_enter_browse(e):
    e.widget["bg"] = "#5F9EA0"  # Cadet Blue
    e.widget["cursor"] = "hand2"

def on_leave_browse(e):
    e.widget["bg"] = "#4682B4"  # Steel Blue

def on_enter_convert(e):
    e.widget["bg"] = "#FF8C00"  # Orange Red
    e.widget["cursor"] = "hand2"

def on_leave_convert(e):
    e.widget["bg"] = "#FF4500"  # Dark Orange

# --- Function to browse markdown file ---
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
    path_entry.delete(0, tk.END)
    path_entry.insert(0, file_path)

# --- Function to convert to HTML ---
def convert_markdown():
    input_path = path_entry.get()
    if not input_path.endswith(".md"):
        messagebox.showerror("Error", "Please select a Markdown (.md) file.")
        return
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
        html_text = markdown.markdown(md_text)

        save_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
        if save_path:
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(html_text)
            messagebox.showinfo("Success", "Markdown successfully converted to HTML!")
            path_entry.delete(0, tk.END)  # Clear the entry box

    except Exception as e:
        messagebox.showerror("Error", f"Conversion failed:\n{e}")

# --- Main Window Setup ---
root = tk.Tk()
root.title("Techno Hacks Intern Markdown to HTML Converter")
root.geometry("600x320")
root.configure(bg="#7FFFD4")  # Aquamarine

# --- Icon and Title ---
icon_label = tk.Label(root, text="", font=("Arial", 30), bg="#7FFFD4", fg="#333333")
icon_label.pack(pady=(20, 0))

title_label = tk.Label(root, text="📝 Markdown to HTML Converter", font=("Arial", 26, "bold"), bg="#7FFFD4", fg="#000000")
title_label.pack(pady=(0, 20))

# --- Entry and Browse Button ---
frame = tk.Frame(root, bg="#7FFFD4")
frame.pack(pady=10)

path_entry = tk.Entry(frame, width=40, font=("Arial", 12))
path_entry.pack(side=tk.LEFT, padx=10)

browse_button = tk.Button(frame, text="Browse", command=browse_file,
                          bg="#4682B4", fg="white", font=("Arial", 11, "bold"))
browse_button.pack(side=tk.LEFT)

browse_button.bind("<Enter>", on_enter_browse)
browse_button.bind("<Leave>", on_leave_browse)

# --- Convert Button ---
convert_btn = tk.Button(root, text="Convert Now", command=convert_markdown,
                        bg="#FF8C00", fg="white", font=("Arial", 14, "bold"), width=20)
convert_btn.pack(pady=20)

convert_btn.bind("<Enter>", on_enter_convert)
convert_btn.bind("<Leave>", on_leave_convert)

# --- Instruction ---
instruction_label = tk.Label(root, text="📂 Browse a Markdown file (.md file) to convert into HTML",
                             bg="#7FFFD4", fg="#000000", font=("Arial", 16, "bold"))
instruction_label.pack(pady=10)

root.mainloop()
