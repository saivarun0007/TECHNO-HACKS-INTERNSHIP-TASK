# 🧭 Text-Based RPG Game

Welcome to **The Lost Library Adventure**, a text-based RPG game developed using **Python** and **Tkinter** as part of the **TechnoHacks internship** project.

This game combines storytelling with simple decision-making logic, interactive buttons, and visuals to create an engaging player experience.

---

## 🎮 Game Features

- 🖱️ **Choice-Based Adventure**: Navigate through multiple story paths based on your decisions.
- 🖼️ **Visual Scenes**: Each stage is accompanied by a relevant image (stored in the `images/` folder).
- 🔁 **Branching Outcomes**: Your decisions lead to different endings—some rewarding, some… not so much.
- 🧠 **Easy to Extend**: Easily add more story stages, images, and outcomes.

---

### 📂 Folder Structure

|--Exe.folder                            # Exe files<br>
|--Text-Based RPG Game.py                # Main Python file with GUI logic<br>
|--README.md                             # Project documentation<br>
|--License                               # Project license <br>
├── images/                              # Required images <br>
  ├── map.jpg<br>
  ├── fork_in_road.jpg<br>
  ├── wise_old_man.jpg<br>
  ├── hidden_cave.jpg<br>
  ├── river.jpg<br>
  ├── village.jpg<br>
  ├── treasure.jpg<br>
  └── lost.jpg<br>

**Note**: Ensure all images are placed inside the `images/` folder for the game to run correctly.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed

- Required libraries:
  ```bash
  pip install pillow
  ```

---

### Run the Game

- python "Text-Based RPG Game_Main Program File.py"

---

## 🛠️ How It Works
- The game is built using tkinter.Tk and starts with an introduction screen.

- Each stage presents a scenario with two choices.

- Based on the user's input, the story progresses through branching logic defined in self.next_stages.

- The outcomes are either a treasure (success) or getting lost (failure).

---

### 🙋‍♂️ Author
**CHANDRUPATLA SAI VARUN**
Developed as part of **Techno Hacks Internship** Program

---
