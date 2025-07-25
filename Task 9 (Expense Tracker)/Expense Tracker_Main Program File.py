import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os
import calendar

# File for storing data
DATA_FILE = "expenses_data.json"

# Load existing data or initialize
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)
with open(DATA_FILE, "r") as f:
    expenses_data = json.load(f)

# Store last removed value
last_removed = {"amount": 0, "desc": ""}

# Hover effects
def on_enter(e):
    if "Add" in e.widget["text"]:
        e.widget["bg"] = "#90EE90"
    elif "Remove" in e.widget["text"]:
        e.widget["bg"] = "#FFAE42"
    elif "Clear" in e.widget["text"]:
        e.widget["bg"] = "#7D0552"
    elif "Exit" in e.widget["text"]:
        e.widget["bg"] = "#F62817"
def on_leave(e):
    if "Add" in e.widget["text"]:
        e.widget["bg"] = "#00FF00"
    elif "Remove" in e.widget["text"]:
        e.widget["bg"] = "#FFA500"
    elif "Clear" in e.widget["text"]:
        e.widget["bg"] = "#800080"
    elif "Exit" in e.widget["text"]:
        e.widget["bg"] = "#FF0000"

# Core functions
def get_date_key():
    return selected_date.get()

def is_editable():
    return datetime.now().strftime("%Y-%m-%d") == selected_date.get()

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(expenses_data, f, indent=2)

def update_middle_display():
    key = get_date_key()
    entries = expenses_data.get(key, [])
    total = sum(e['amount'] for e in entries)
    add_amount = entries[-1]['amount'] if entries else 0
    desc = entries[-1]['desc'] if entries else ''
    removed_amt = last_removed['amount']

    middle_display.config(state="normal")
    middle_display.delete("1.0", tk.END)
    middle_display.insert(tk.END, f"Add Expense:       ₹{add_amount}\n\n")
    middle_display.insert(tk.END, f"Removed Expense:    ₹{removed_amt}\n\n")
    middle_display.insert(tk.END, f"View Expense:      ₹{total}\n\n")
    middle_display.insert(tk.END, f"Description:       {desc}\n\n")
    middle_display.insert(tk.END, f"Total Expense:     ₹{total}")
    middle_display.config(state="disabled")

    update_total_label()

def update_total_label():
    total = sum(entry['amount'] for day in expenses_data.values() for entry in day)
    total_label.config(text=f"💰 Total (All Days): ₹{total}")

def add_expense():
    if not is_editable():
        return
    try:
        amt = float(amount_entry.get())
        desc = desc_entry.get()
        if not desc:
            raise ValueError
        entry = {"amount": amt, "desc": desc}
        key = get_date_key()
        expenses_data.setdefault(key, []).append(entry)
        save_data()
        update_middle_display()
        amount_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Enter valid amount and description.")

def remove_expense():
    if not is_editable():
        return
    key = get_date_key()
    if key in expenses_data and expenses_data[key]:
        removed = expenses_data[key].pop()
        last_removed['amount'] = removed['amount']
        last_removed['desc'] = removed['desc']
        save_data()
        update_middle_display()

def clear_expenses():
    if not is_editable():
        return
    key = get_date_key()
    if key in expenses_data:
        expenses_data[key] = []
        last_removed['amount'] = 0
        last_removed['desc'] = ''
        save_data()
        update_middle_display()

def update_selected_date(*args):
    update_middle_display()
    editable = is_editable()
    add_btn.config(state="normal" if editable else "disabled")
    remove_btn.config(state="normal" if editable else "disabled")
    clear_btn.config(state="normal" if editable else "disabled")

# Window setup
root = tk.Tk()
root.title("Techno Hacks Intern Expense Tracker")
root.geometry("900x650")
root.config(bg="#C35817")

selected_date = tk.StringVar()

# --- Top (Calendar) ---
top_frame = tk.Frame(root, bg="#C35817")
top_frame.pack(pady=10)

def create_date_selector(frame):
    today = datetime.today()
    years = list(range(2025, 2076))
    months = list(calendar.month_name)[1:]
    days = list(range(1, 32))

    def set_date(*_):
        try:
            month_number = list(calendar.month_name).index(month.get())
            dt = datetime(year.get(), month_number, day.get())
            selected_date.set(dt.strftime("%Y-%m-%d"))
        except:
            pass

    year = tk.IntVar(value=today.year)
    month = tk.StringVar(value=calendar.month_name[today.month])
    day = tk.IntVar(value=today.day)

    tk.Label(frame, text="📅 EXPENSE TRACKER ₹", font=("Algerian", 28, "bold"), bg="#C35817", fg="BLACK").grid(row=0, column=0, columnspan=6, pady=(0, 20))

    tk.Label(frame, text="YEAR:", font=("Arial", 20, "bold"), width=6, bg="#C35817", fg="black").grid(row=1, column=0, padx=10, pady=10)
    ttk.Combobox(frame, values=years, textvariable=year, font=("Arial", 16), width=8).grid(row=1, column=1, padx=10)

    tk.Label(frame, text="MONTH:", font=("Arial", 20, "bold"), width=6, bg="#C35817", fg="black").grid(row=1, column=2, padx=10, pady=10)
    ttk.Combobox(frame, values=months, textvariable=month, font=("Arial", 16), width=10).grid(row=1, column=3, padx=10)

    tk.Label(frame, text="DAY:", font=("Arial", 20, "bold"), width=6, bg="#C35817", fg="black").grid(row=1, column=4, padx=10, pady=10)
    ttk.Combobox(frame, values=days, textvariable=day, font=("Arial", 16), width=6).grid(row=1, column=5, padx=10)

    for var in (year, month, day):
        var.trace_add("write", set_date)

    set_date()

create_date_selector(top_frame)
selected_date.trace_add("write", update_selected_date)

# --- Input Section ---
input_frame = tk.Frame(root, bg="#C35817")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Amount ₹*:", font=("Arial", 18, "bold"), bg="#C35817").grid(row=0, column=0, padx=5)
amount_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
amount_entry.grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="Description*:", font=("Arial", 18, "bold"), bg="#C35817").grid(row=0, column=2, padx=5)
desc_entry = tk.Entry(input_frame, font=("Arial", 12), width=25)
desc_entry.grid(row=0, column=3, padx=5)

# --- Button Row ---
btn_frame = tk.Frame(root, bg="#C35817")
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Add Expense", font=("Arial", 16, "bold"), bg="#00FF00", fg="black", width=15, command=add_expense)
remove_btn = tk.Button(btn_frame, text="Remove Last", font=("Arial", 16, "bold"), bg="#FFA500", fg="black", width=15, command=remove_expense)
clear_btn = tk.Button(btn_frame, text="Clear All", font=("Arial", 16, "bold"), bg="#800080", fg="white", width=15, command=clear_expenses)

for btn in [add_btn, remove_btn, clear_btn]:
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

add_btn.grid(row=0, column=0, padx=10)
remove_btn.grid(row=0, column=1, padx=10)
clear_btn.grid(row=0, column=2, padx=10)

# --- Middle Display Area ---
middle_frame = tk.Frame(root, bg="#C35817")
middle_frame.pack(pady=10)

middle_display = tk.Text(middle_frame, height=10, width=60, font=("Algerian", 16, "bold"), bg="#e8f5e9", state="disabled")
middle_display.pack()

tk.Label(middle_frame, text="* All data will be saved into a expenses_data.JSON file automatically", 
         font=("Arial", 19, "bold", "italic"), fg="white", bg="#C35817").pack(pady=(5, 0))


# --- Bottom Area with Exit and Total ---
bottom_frame = tk.Frame(root, bg="#C35817")
bottom_frame.pack(side="bottom", fill="x", pady=15)

exit_btn = tk.Button(bottom_frame, text="Exit", font=("Arial", 12, "bold"), bg="#FF0000", fg="white", width=10, command=root.quit)
exit_btn.pack(side="left", padx=20)
exit_btn.bind("<Enter>", on_enter)
exit_btn.bind("<Leave>", on_leave)

total_label = tk.Label(bottom_frame, text="💰 Total (All Days): ₹0", font=("Arial", 20, "bold"), bg="#ffff00", fg="black")
total_label.pack(side="right", padx=20)

# Load first view
update_selected_date()
root.mainloop()