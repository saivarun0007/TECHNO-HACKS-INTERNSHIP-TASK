import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Quiz Data 
questions = [
     {
        "question": "What is the output of: print(type([]))?",
        "options": ["<class 'list'>", "<class 'dict'>", "<class 'set'>", "<class 'tuple'>"],
        "answer": "<class 'list'>"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["function", "def", "lambda", "fun"],
        "answer": "def"
    },
    {
        "question": "Which of the following is a mutable data type?",
        "options": ["tuple", "str", "list", "int"],
        "answer": "list"
    },
    {
        "question": "What will be the output of: print(2 ** 3 ** 2)?",
        "options": ["64", "512", "256", "8"],
        "answer": "512"
    },
    {
        "question": "Which of the following is not a Python keyword?",
        "options": ["with", "assert", "pass", "eval"],
        "answer": "eval"
    },
    {
        "question": "Which function is used to get the length of a list in Python?",
        "options": ["count()", "size()", "length()", "len()"],
        "answer": "len()"
    },
    {
        "question": "How do you start a comment in Python?",
        "options": ["//", "<!--", "#", "/*"],
        "answer": "#"
    },
    {
        "question": "What does the 'break' statement do in loops?",
        "options": ["Skips one iteration", "Terminates the loop", "Pauses the loop", "Restarts the loop"],
        "answer": "Terminates the loop"
    },
    {
        "question": "Which operator is used for floor division?",
        "options": ["/", "%", "//", "**"],
        "answer": "//"
    },
    {
        "question": "What is the correct way to define a class in Python?",
        "options": ["class MyClass:", "def class MyClass():", "class MyClass[]:", "MyClass class():"],
        "answer": "class MyClass:"
    }
]

# Globals
current_index = 0
score = 0
timer_seconds = 15
timer_id = None

# GUI Setup 
root = tk.Tk()
selected = tk.StringVar()
root.title("Techno Hacks Intern Quiz Application")
root.geometry("800x600")
root.config(bg="#FFFF00")

# Frames
start_frame = tk.Frame(root, bg="#FFFF00")
rules_frame = tk.Frame(root, bg="#FFFF00")
quiz_frame = tk.Frame(root, bg="#E2F516")
final_frame = tk.Frame(root, bg="#FFFF00")

for frame in (start_frame, rules_frame, quiz_frame, final_frame):
    frame.place(relwidth=1, relheight=1)

# Functions
def show_frame(frame):
    frame.tkraise()

def start_quiz():
    show_frame(rules_frame)

def quit_app():
    root.destroy()

def continue_to_quiz():
    show_frame(quiz_frame)
    load_question()

def load_question():
    global timer_seconds, timer_id
    selected.set(None)
    q = questions[current_index]
    question_label.config(text=f"Q{current_index+1}: {q['question']}")
    for i, opt in enumerate(q['options']):
        option_buttons[i].config(text=opt, bg="white", state="normal")
    timer_seconds = 15
    update_timer()
    next_btn.config(state="disabled")

def update_timer():
    global timer_seconds, timer_id
    timer_label.config(text=f"⏱️ {timer_seconds} sec")
    if timer_seconds > 0:
        timer_seconds -= 1
        timer_id = root.after(1000, update_timer)
    else:
        reveal_answer()

def option_selected(index):
    global score
    if timer_id:
        root.after_cancel(timer_id)

    selected_val = option_buttons[index].cget("text")
    correct = questions[current_index]["answer"]
    for btn in option_buttons:
        btn.config(state="disabled")

    if selected_val == correct:
        option_buttons[index].config(bg="#00FF00")
        score += 5
    else:
        option_buttons[index].config(bg="red")
        score -= 2
        for btn in option_buttons:
            if btn.cget("text") == correct:
                btn.config(bg="#00FF00")
    score_label.config(text=f"Score: {score}")
    next_btn.config(state="normal")

def reveal_answer():
    correct = questions[current_index]["answer"]
    for btn in option_buttons:
        btn.config(state="disabled")
        if btn.cget("text") == correct:
            btn.config(bg="#00FF00")
    score_label.config(text=f"Score: {score}")
    next_btn.config(state="normal")

def next_question():
    global current_index
    current_index += 1
    if current_index < len(questions):
        load_question()
    else:
        show_final()

def show_final():
    final_score_label.config(text=f"Your Final Score: {score}/{len(questions)*5}")
    show_frame(final_frame)

def restart():
    global current_index, score
    current_index = 0
    score = 0
    score_label.config(text=f"Score: {score}")
    show_frame(start_frame)

# Start Frame
logo_img_pil = Image.open("logo.png")  
logo_img_pil = logo_img_pil.resize((600, 400)) 
logo_img = ImageTk.PhotoImage(logo_img_pil)  

logo_label = tk.Label(start_frame, image=logo_img, bg="#FFFF00")
logo_label.image = logo_img 
logo_label.pack(pady=20)

start_btn = tk.Button(start_frame, text="Start Quiz", font=("Arial", 14, "bold"), bg="#FFFF00", fg="black",
                      activebackground="#E2F516", cursor="hand2", width=15, height=2, command=start_quiz)
start_btn.pack()

start_btn.bind("<Enter>", lambda e: start_btn.config(bg="#E2F516"))
start_btn.bind("<Leave>", lambda e: start_btn.config(bg="#FFFF00"))

# Rules Frame
rules_title = tk.Label(rules_frame, text="📒 Rules of this Quiz 📒", font=("Lato", 26, "bold"), bg="#FFFF00", fg="#222")
rules_title.pack(pady=(10, 5))
tk.Frame(rules_frame, height=2, bg="#E2F516").pack(fill="x")
tk.Frame(rules_frame, height=2, bg="#E2F516").pack(fill="x")
tk.Frame(rules_frame, height=2, bg="black").pack(fill="x")
tk.Frame(rules_frame, height=2, bg="#FFFF00").pack(fill="x")
tk.Frame(rules_frame, height=2, bg="black").pack(fill="x")
tk.Frame(rules_frame, height=2, bg="#E2F516").pack(fill="x")
tk.Frame(rules_frame, height=2, bg="#E2F516").pack(fill="x")

rules_lines = [
    ("1. You will have only ", "15 seconds", " per each question."),
    ("2. Once you select your answer, it can't be undone.",),
    ("3. You can't select any option once time goes off.",),
    ("4. You can exit from the Quiz while you're playing.",),
    ("5. You'll get points on the basis of your answers:",),
    ("              ✨ Right Answer: ", "+5 Points"),
    ("              ✨ Wrong Answer: ", "-2 Points"),
    ("              ✨ No Answer: ", "0 Points")
]
rules_list = tk.Frame(rules_frame, bg="#FFFF00")
rules_list.pack(pady=20)

for rule in rules_lines:
    line = tk.Label(rules_list, bg="#FFFF00")
    line.pack(anchor="w", padx=20, pady=2)
    for part in rule:
        color = "red" if "15" in part else ("green" if "+5" in part else ("#00008B" if "-2" in part else ("#800080" if "0" in part else "black")))
        lbl = tk.Label(line, text=part, font=("Lato", 18, "bold" if color != "black" else "normal"), fg=color, bg="#FFFF00")
        lbl.pack(side="left")

btn_frame = tk.Frame(rules_frame, bg="#FFFF00")
btn_frame.pack(pady=10)

quit_btn = tk.Button(btn_frame, text="I QUIT", command=quit_app, bg="#FFFF00", fg="#FF0000", font=("Lato", 16, "bold"),
                     relief="solid", borderwidth=2, width=14, height=2)
quit_btn.grid(row=0, column=0, padx=10)
quit_btn.bind("<Enter>", lambda e: quit_btn.config(bg="#fdd"))
quit_btn.bind("<Leave>", lambda e: quit_btn.config(bg="#FFFF00"))

continue_btn = tk.Button(btn_frame, text="CONTINUE", command=continue_to_quiz, bg="#FFFF00", fg="green", font=("Lato", 16, "bold"),
                         relief="solid", borderwidth=2, width=14, height=2)
continue_btn.grid(row=0, column=1, padx=10)
continue_btn.bind("<Enter>", lambda e: continue_btn.config(bg="#dfd"))
continue_btn.bind("<Leave>", lambda e: continue_btn.config(bg="#FFFF00"))

# Quiz Frame 
top_bar = tk.Frame(quiz_frame, bg="#E2F516")
top_bar.pack(pady=20, fill="x")

score_label = tk.Label(top_bar, text="Score: 0", font=("Arial", 18, "bold"), bg="#E2F516")
score_label.pack(side="left", padx=20)

title_label = tk.Label(top_bar, text="📝 Quiz Application 📝", font=("Arial", 26, "bold"), bg="#E2F516")
title_label.pack(side="top")

timer_label = tk.Label(top_bar, text="⏱️ 15 sec", font=("Arial", 18, "bold"), bg="#E2F516")
timer_label.pack(side="right", padx=20)

question_label = tk.Label(quiz_frame, text="", font=("Arial", 16), wraplength=650, bg="#E2F516")
question_label.pack(pady=30)

option_buttons = []
for i in range(4):
    btn = tk.Button(quiz_frame, text="", font=("Arial", 12), width=50, height=2, command=lambda idx=i: option_selected(idx))
    btn.pack(pady=5)
    option_buttons.append(btn)

bottom_bar = tk.Frame(quiz_frame, bg="#E2F516")
bottom_bar.pack(side="bottom", fill="x", pady=10)

quit_quiz_btn = tk.Button(bottom_bar, text="Quit",font=("Arial", 16), command=quit_app, bg="#FF0000")
quit_quiz_btn.pack(side="left", padx=20)

next_btn = tk.Button(bottom_bar, text="Next Question ▶▶▶", font=("Arial", 16), bg="#00FF00", command=next_question, state="disabled")
next_btn.pack(side="right", padx=20)

# Final Frame 
final_score_label = tk.Label(final_frame, text="", font=("Arial", 26, "bold"), bg="#FFFF00")
final_score_label.pack(pady=60)

final_btn_frame = tk.Frame(final_frame, bg="#FFFF00")
final_btn_frame.pack()

replay_btn = tk.Button(final_btn_frame, text="Replay", font=("Arial", 18, "bold"), bg="#00FF00", fg="black", command=restart)
replay_btn.grid(row=0, column=0, padx=20)
replay_btn.bind("<Enter>", lambda e: replay_btn.config(bg="#34A56F", fg="white"))
replay_btn.bind("<Leave>", lambda e: replay_btn.config(bg="#00FF00", fg="black"))

exit_btn = tk.Button(final_btn_frame, text="Quit", font=("Arial", 18, "bold"), bg="red", fg="white", command=quit_app)
exit_btn.grid(row=0, column=1, padx=20)
exit_btn.bind("<Enter>", lambda e: exit_btn.config(bg="#cc0000", fg="black"))
exit_btn.bind("<Leave>", lambda e: exit_btn.config(bg="red", fg="white"))

# Start App
show_frame(start_frame)
root.mainloop()
