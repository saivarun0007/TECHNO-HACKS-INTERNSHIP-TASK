import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
import time

from PIL import Image, ImageTk  # Ensure this is imported at the top

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Techno Hacks Intern To-Do-List App")
        self.root.geometry("500x600")
        self.root.configure(bg="#FF00FF")  # Nice background color

        # ✅ Load logo.png and resize
        logo_img = Image.open("logo.png")
        logo_img = logo_img.resize((60, 60), Image.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(logo_img)

        # ✅ Title Label with image + text
        self.title_label = tk.Label(
            root,
            text="TO-DO-LIST",
            image=self.logo_photo,
            compound=tk.LEFT,
            font=("Arial", 24, "bold"),
            bg="#FF00FF",
            fg="black",
            pady=5
        )
        self.title_label.pack(pady=10, fill="x")

        self.tasks = []


        #self.title_label = tk.Label(root, text="📝 To-Do List", font=("Arial", 20, "bold"), bg="#e0f7fa", fg="#006064")
        #self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(root, font=("Arial", 14), width=30, bg="#ffffff")
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", font=("Arial", 12), bg="#000000", fg="white", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_frame = tk.Frame(root, bg="#e0f7fa")
        self.task_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Input Error", "Please enter a task.")
            return

        self.task_entry.delete(0, tk.END)

        task_number = len(self.tasks) + 1
        task_frame = tk.Frame(self.task_frame, bg="#ffffff", pady=5)
        task_frame.pack(fill=tk.X, padx=10, pady=5)

        var = tk.BooleanVar()

        check = tk.Checkbutton(task_frame, variable=var, command=lambda: self.complete_task(check, label, var, edit_button), bg="#ffffff")
        check.pack(side=tk.LEFT)

        label = tk.Label(task_frame, text=f"{task_number}. {task_text}", font=("Arial", 12), bg="#ffffff", anchor="w")
        label.pack(side=tk.LEFT, fill=tk.X, expand=True)

        edit_button = tk.Button(task_frame, text="Edit", bg="#0288D1", fg="white", command=lambda: self.edit_task(label))
        edit_button.pack(side=tk.RIGHT, padx=5)

        delete_button = tk.Button(task_frame, text="Delete", bg="#D32F2F", fg="white", command=lambda: self.delete_task(task_frame))
        delete_button.pack(side=tk.RIGHT, padx=5)

        self.tasks.append({
            "frame": task_frame,
            "label": label,
            "checkbox": check,
            "edit_button": edit_button,
            "delete_button": delete_button,
            "var": var
        })

    def edit_task(self, label):
        updated_text = simpledialog.askstring("Edit Task", "Update task:", initialvalue=label.cget("text")[label.cget("text").find('.')+2:])
        if updated_text:
            task_number = label.cget("text").split('.')[0]
            label.config(text=f"{task_number}. {updated_text}")

    def delete_task(self, frame):
        if messagebox.askyesno("Delete", "Are you sure you want to delete this task?"):
            frame.destroy()

    def complete_task(self, checkbox, label, var, edit_button):
        if var.get():
            # Disable editing
            edit_button.config(state=tk.DISABLED)

            # Blasting effect (simulated)
            def animate_blast():
                original_color = label.cget("fg")
                colors = ["#FF0000", "#00FFFF", "#0000FF", "#00008B", "#ADD8E6", "#800080", "#FFFF00", "#00FF00",
                          "#FFFFFF", "#C0C0C0", "#808080", "#000000", "#FFA500", "#A52A2A", "#800000", "#008000",
                          "#FF00FF", "#FFC0CB", "#808000", "#7FFFD4"]
                for color in colors:
                    time.sleep(0.05)
                    label.config(fg=color)
                label.config(fg="gray", text="✔️ " + label.cget("text"), font=("Arial", 12, "overstrike"))
                checkbox.config(state=tk.DISABLED)

            threading.Thread(target=animate_blast).start()
        else:
            label.config(fg="black", font=("Arial", 12), text=label.cget("text").replace("✔️ ", ""))
            checkbox.config(state=tk.NORMAL)
            edit_button.config(state=tk.NORMAL)

# Launch App
root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
