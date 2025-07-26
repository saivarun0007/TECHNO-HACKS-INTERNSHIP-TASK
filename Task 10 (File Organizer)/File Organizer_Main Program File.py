import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

# --- File type categories ---
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".svg", ".ico", ".heic", ".raw"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv", ".md", ".log", ".epub", ".json", ".xml", ".yml", ".yaml"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".3gp", ".m4v", ".ts", ".f4v", ".mpeg", ".mpg"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".alac", ".aiff", ".opus", ".amr"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".tar.gz", ".bz2", ".xz", ".tar.xz", ".iso", ".dmg", ".cab", ".lz", ".z"]
}

# --- Placeholder text ---
PLACEHOLDER_TEXT = "Browse the path to Organizer"

# --- Get file category ---
def get_category(file_extension):
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"

# --- Organize files ---
def organize_files(folder_path, status_label):
    if not folder_path or folder_path == PLACEHOLDER_TEXT:
        messagebox.showerror("Error", "Please select a valid folder.")
        return

    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                file_ext = os.path.splitext(filename)[1]
                category = get_category(file_ext)
                category_folder = os.path.join(folder_path, category)

                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)

                shutil.move(file_path, os.path.join(category_folder, filename))

        status_label.config(text="✅ Files organized successfully!", foreground="green")
    except Exception as e:
        status_label.config(text=f"❌ Error: {e}", foreground="red")

# --- Browse folder ---
def browse_folder(entry, status_label):
    folder = filedialog.askdirectory()
    if folder:
        entry.config(state="normal")
        entry.delete(0, tk.END)
        entry.insert(0, folder)
        entry.config(fg="black", state="readonly")
        status_label.config(text="📁 Folder selected. Ready to organize.", foreground="orange")

# --- GUI Design ---
def build_gui():
    root = tk.Tk()
    root.title("Techno Hacks Intern Messi File Organizer")
    root.geometry("600x300")
    root.resizable(False, False)
    root.config(bg="#1e1e2f")  # Dark background

    # --- Style ---
    style = ttk.Style()
    style.theme_use("default")

    # Browse Button Style (Sky Blue)
    style.configure("Browse.TButton",
                    font=("Segoe UI", 12, "bold"),
                    padding=10,
                    foreground="black",
                    background="#00BFFF")
    style.map("Browse.TButton",
              background=[("active", "#87CEFA")])

    # Organize Button Style (Light Green)
    style.configure("Organize.TButton",
                    font=("Segoe UI", 12, "bold"),
                    padding=10,
                    foreground="black",
                    background="#32CD32")
    style.map("Organize.TButton",
              background=[("active", "#90EE90")])

    # --- Heading ---
    heading = tk.Label(root, text="🗂️ Messi File Organizer", font=("Segoe UI", 26, "bold"),
                       bg="#1e1e2f", fg="#ffff00")
    heading.pack(pady=20)

    # --- Path Frame ---
    path_frame = tk.Frame(root, bg="#1e1e2f")
    path_frame.pack(pady=10)

    folder_entry = tk.Entry(path_frame, font=("Segoe UI", 12), width=40,
                            bg="white", fg="black", insertbackground="black", relief="solid", state="normal")
    folder_entry.pack(side=tk.LEFT, padx=10)
    folder_entry.insert(0, PLACEHOLDER_TEXT)
    folder_entry.config(state="readonly")

    # --- Placeholder logic ---
    def on_entry_click(event):
        if folder_entry.get() == PLACEHOLDER_TEXT:
            folder_entry.config(state="normal")
            folder_entry.delete(0, tk.END)
            folder_entry.config(fg="black")

    def on_focusout(event):
        if not folder_entry.get():
            folder_entry.config(state="normal")
            folder_entry.insert(0, PLACEHOLDER_TEXT)
            folder_entry.config(fg="gray", state="readonly")

    folder_entry.bind("<FocusIn>", on_entry_click)
    folder_entry.bind("<FocusOut>", on_focusout)

    # --- Browse Button ---
    browse_btn = ttk.Button(path_frame, text="Browse", style="Browse.TButton",
                            command=lambda: browse_folder(folder_entry, status_label))
    browse_btn.pack(side=tk.LEFT)

    # --- Organize Button ---
    organize_btn = ttk.Button(root, text="Organize Now", style="Organize.TButton",
                              command=lambda: organize_files(folder_entry.get(), status_label))
    organize_btn.pack(pady=20)

    # --- Status Label ---
    global status_label
    status_label = tk.Label(root, text="📁 Browse or select a folder to organize files.",
                            font=("Segoe UI", 12), bg="#1e1e2f", fg="orange")
    status_label.pack()

    root.mainloop()

# --- Run ---
if __name__ == "__main__":
    build_gui()
