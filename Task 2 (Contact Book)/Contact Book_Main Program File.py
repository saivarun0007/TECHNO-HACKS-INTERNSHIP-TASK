import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
import re

# --- Hover Effects ---
def on_enter(e):
    e.widget["bg"] = "#000000"
    e.widget["activebackground"] = "#FFA500"

def on_leave(e):
    e.widget["bg"] = "#FFA500"
    e.widget["activebackground"] = "#000000"

# --- Open Contact Book ---
def open_contact_book():
    login_window.destroy()
    root = tk.Tk()
    root.title("Techno Hacks Intern Contact Book")
    root.geometry("600x600")
    root.config(bg="#FFA500")

    label_opts = {"bg": "#FFA500", "fg": "black", "font": ("Arial", 12)}
    entry_opts = {"width": 40}

    def validate_phone(phone):
        return bool(re.fullmatch(r"\+\d{12}", phone))

    def validate_email(email):
        return bool(re.fullmatch(r"[a-zA-Z0-9._%+-]+@gmail\.com", email))

    def save_contact():
        fname = entry_fname.get()
        lname = entry_lname.get()
        phone = entry_phone.get()
        email = entry_email.get()
        address = entry_address.get()

        if not fname or not phone:
            messagebox.showwarning("Missing Info", "First Name and Phone are required.")
            return

        if not validate_phone(phone):
            messagebox.showerror("Invalid Phone", "Phone must start with '+' and be 13 characters (e.g., +911234567890)")
            return

        if email and not validate_email(email):
            messagebox.showerror("Invalid Email", "Only valid Gmail addresses allowed (e.g., user@gmail.com)")
            return

        try:
            file_exists = False
            with open("contacts.csv", "r") as file:
                file_exists = True
        except FileNotFoundError:
            pass

        with open("contacts.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["First Name", "Last Name", "Phone", "Email", "Address"])
            writer.writerow([fname, lname, phone, email, address])

        messagebox.showinfo("Saved", "Contact saved successfully!")
        clear_entries()

    def search_contact():
        search_text = entry_search.get().lower()
        output = ""
        try:
            with open("contacts.csv", "r") as file:
                reader = csv.reader(file)
                rows = list(reader)
                for i in range(1, len(rows)):
                    if any(search_text in field.lower() for field in rows[i]):
                        output += (
                            f"First Name: {rows[i][0]}\n"
                            f"Last Name: {rows[i][1]}\n"
                            f"Phone: {rows[i][2]}\n"
                            f"Email: {rows[i][3]}\n"
                            f"Address: {rows[i][4]}\n\n"
                        )
            label_search_output.config(text=output if output else "No match found.")
        except FileNotFoundError:
            label_search_output.config(text="Contact file not found.")

    def delete_contact():
        search_text = entry_search.get().lower()
        found = False
        try:
            with open("contacts.csv", "r") as file:
                reader = csv.reader(file)
                rows = list(reader)
            new_rows = [rows[0]]
            for row in rows[1:]:
                if any(search_text in field.lower() for field in row):
                    found = True
                    continue
                new_rows.append(row)
            with open("contacts.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(new_rows)
            label_search_output.config(text="Contact deleted." if found else "No matching contact found.")
        except FileNotFoundError:
            label_search_output.config(text="Contact file not found.")

    def clear_entries():
        entry_fname.delete(0, tk.END)
        entry_lname.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)

    def exit_app():
        root.destroy()

    def create_button(text, command, row, col):
        btn = tk.Button(
            root, text=text, command=command, bg="#FFA500", fg="white",
            activebackground="black", activeforeground="white",
            font=("Arial", 12), relief="raised", bd=4, width=12
        )
        btn.grid(row=row, column=col, padx=10, pady=10)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        return btn

    # --- Input Fields ---
    tk.Label(root, text="Enter First Name", **label_opts).grid(row=0, column=0, sticky="w", padx=10, pady=5)
    entry_fname = tk.Entry(root, **entry_opts)
    entry_fname.grid(row=0, column=1, padx=10)

    tk.Label(root, text="Enter Last Name", **label_opts).grid(row=1, column=0, sticky="w", padx=10, pady=5)
    entry_lname = tk.Entry(root, **entry_opts)
    entry_lname.grid(row=1, column=1, padx=10)

    tk.Label(root, text="Enter Phone Number", **label_opts).grid(row=2, column=0, sticky="w", padx=10, pady=5)
    entry_phone = tk.Entry(root, **entry_opts)
    entry_phone.grid(row=2, column=1, padx=10)

    tk.Label(root, text="Enter Email", **label_opts).grid(row=3, column=0, sticky="w", padx=10, pady=5)
    entry_email = tk.Entry(root, **entry_opts)
    entry_email.grid(row=3, column=1, padx=10)

    tk.Label(root, text="Enter Address", **label_opts).grid(row=4, column=0, sticky="w", padx=10, pady=5)
    entry_address = tk.Entry(root, **entry_opts)
    entry_address.grid(row=4, column=1, padx=10)

    create_button("Save", save_contact, 5, 0)
    create_button("Cancel", exit_app, 5, 1)

    tk.Label(root, text="Search by", **label_opts).grid(row=6, column=0, sticky="w", padx=10, pady=5)
    entry_search = tk.Entry(root, **entry_opts)
    entry_search.grid(row=6, column=1, padx=10)

    create_button("Search", search_contact, 7, 0)
    create_button("Delete", delete_contact, 7, 1)

    label_search_output = tk.Label(root, text="", wraplength=500, justify="left", font=("Arial", 12),
                                   bg="#FFA500", fg="black")
    label_search_output.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

# --- Login Validation ---
def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    if len(password) < 6 or not re.search(r"[A-Za-z]", password) \
            or not re.search(r"[0-9]", password) or not re.search(r"[\W_]", password):
        messagebox.showerror("Weak Password", "Password must include letters, numbers, and symbols.")
        return

    if username.strip() == "" or password.strip() == "":
        messagebox.showerror("Login Failed", "Please enter both fields.")
        return

    open_contact_book()

# --- Login Window ---
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("400x500")
login_window.config(bg="#FFA500")

# --- Optional Logo ---
try:
    img = Image.open("logo.png")
    img = img.resize((100, 100))
    logo = ImageTk.PhotoImage(img)
    tk.Label(login_window, image=logo, bg="#FFA500").pack(pady=20)
except Exception:
    tk.Label(login_window, text="[Logo Missing]", bg="#FFA500", fg="white", font=("Arial", 12)).pack(pady=20)

# --- Login Form ---
tk.Label(login_window, text="Username", bg="#FFA500", fg="black", font=("Arial", 12)).pack(pady=5)
entry_username = tk.Entry(login_window, width=30)
entry_username.pack(pady=5)

tk.Label(login_window, text="Password", bg="#FFA500", fg="black", font=("Arial", 12)).pack(pady=5)
entry_password = tk.Entry(login_window, show="*", width=30)
entry_password.pack(pady=5)

# --- Login Button ---
login_btn = tk.Button(login_window, text="Login", bg="#FFA500", fg="white",
                      activebackground="black", activeforeground="white",
                      font=("Arial", 12), relief="raised", bd=4, width=12,
                      command=validate_login)
login_btn.pack(pady=20)
login_btn.bind("<Enter>", on_enter)
login_btn.bind("<Leave>", on_leave)

login_window.mainloop()
