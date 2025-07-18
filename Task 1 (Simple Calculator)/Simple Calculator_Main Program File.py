import tkinter as tk

def press(symbol):
    current = entry_var.get()

    if symbol == "=":
        try:
            expression = current.replace("*", "x").replace("÷", "/")
            result = str(eval(expression))
            entry.config(state="normal")
            entry_var.set(result)
            entry.config(state="readonly")
        except:
            entry.config(state="normal")
            entry_var.set("Error")
            entry.config(state="readonly")
    elif symbol == "AC":
        entry.config(state="normal")
        entry_var.set("")
        entry.config(state="readonly")
    elif symbol == "DEL":
        entry.config(state="normal")
        entry_var.set(current[:-1])
        entry.config(state="readonly")
    else:
        entry.config(state="normal")
        entry_var.set(current + symbol)
        entry.config(state="readonly")

# Main Window Configuration
root = tk.Tk()
root.title("Techno Hacks Intern Calculator")
root.geometry("450x650")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# Display Entry --> Read-Only
entry_var = tk.StringVar()
entry = tk.Entry(
    root,
    textvariable=entry_var,
    font=("Arial", 28),
    bd=10,
    relief=tk.RIDGE,
    bg="#f9f9f9",
    justify="right",
    state="readonly"
)
entry.pack(fill="both", ipadx=8, ipady=25, padx=10, pady=20)

# Buttons Layout
buttons = [
    ["AC", "DEL", "%", "÷"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="]
]

# Color Theme
colors = {
    "AC": "#ff5c5c",
    "DEL": "#ff964f",
    "%": "#ff964f",
    "÷": "#4f8cff",
    "*": "#4f8cff",
    "-": "#4f8cff",
    "+": "#4f8cff",
    "=": "#1cc88a",
    "default": "#e0e0e0",
    "text": "#000000",
    "operator_text": "#ffffff"
}

# Buttons UI
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(expand=True, fill="both", padx=10, pady=10)

for row in buttons:
    row_frame = tk.Frame(btn_frame, bg="#1e1e1e")
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        bg_color = colors.get(btn, colors["default"])
# white color text for operators
        operator_buttons = ["+", "-", "*", "÷", "=", "AC", "DEL", "%"]
        fg_color = colors["operator_text"] if btn in operator_buttons else colors["text"]
        button = tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 20, "bold"),
            bg=bg_color,
            fg=fg_color,
            width=5,
            height=2,
            command=lambda b=btn: press(b)
        )
        button.pack(side="left", expand=True, fill="both", padx=2, pady=2)

root.mainloop()
