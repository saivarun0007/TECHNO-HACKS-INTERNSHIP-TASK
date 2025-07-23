import tkinter as tk
from tkinter import messagebox
from random import randint

# Initialize root window
root = tk.Tk()
root.title("Techno Hacks Intern Number Guessing Game")
root.geometry("600x350")

# Tkinter IntVar to get user input
num = tk.StringVar()

# Generate random number once
random_num = randint(1, 100)

# Welcome label
label = tk.Label(root, text="Welcome to Number Guessing Game", font=("Arial", 25, 'bold'))
label.grid(row=0, column=0, columnspan=3, pady=20)

# Submit function
def submit():
    global random_num
    random_num = randint(1, 100)
    user_input = num.get()

    # Clear previous result labels
    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) in (3, 4):
            widget.destroy()

    # Input validation
    if not user_input.isdigit():
        messagebox.showwarning("Invalid Input", "⚠️ Please enter a valid number!")
        return

    user_num = int(user_input)

    if not 1 <= user_num <= 100:
        messagebox.showwarning("Out of Range", "🚫 Please enter a number between 1 and 100!")
        return

    num.set('')  # Clear the input

    if user_num > random_num:
        result_label = tk.Label(root, text="Too High!", font=('Arial', 20, 'bold'), fg="red")
        result_label.grid(row=3, column=0, columnspan=2)
    elif user_num < random_num:
        result_label = tk.Label(root, text="Too Low!", font=('Arial', 20, 'bold'), fg="orange")
        result_label.grid(row=3, column=0, columnspan=2)
    else:
        result_label = tk.Label(root, text="🎉 Congratulations! You guessed right!", font=('Arial', 20, 'bold'), fg="green")
        result_label.grid(row=3, column=0, columnspan=3)

    comp_label = tk.Label(root, text=f"Computer Guess: {random_num}", font=('Arial', 18))
    comp_label.grid(row=4, column=0, columnspan=3)


# Input field
name_label = tk.Label(root, text='Enter a number between 1-100:', font=('calibre', 14, 'bold'))
name_entry = tk.Entry(root, textvariable=num, font=('calibre', 20, 'normal'), width=10)

# Bigger Submit button
sub_btn = tk.Button(root, text='Submit', command=submit, font=('Arial', 14, 'bold'), bg='skyblue', width=12, height=2)

# Grid layout
name_label.grid(row=1, column=0, pady=10)
name_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1, pady=10)

# Run the app
root.mainloop()
