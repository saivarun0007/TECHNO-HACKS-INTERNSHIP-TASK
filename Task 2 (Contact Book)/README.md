# 📒 Contact Book Application

A secure and user-friendly GUI-based Contact Book built using Python's `tkinter`. This project was developed as part of the **Techno Hacks Internship** and showcases form handling, file I/O (CSV), input validation, and login-based access control using regular expressions.

---

## 📌 Features

- 🔐 **Login System** with username & strong password validation
- ✅ Add new contacts (with validations for phone and Gmail addresses)
- 🔍 Search and display contacts
- ❌ Delete existing contacts
- 💾 Save contact information to a `.csv` file
- 🎨 Smooth button hover effects and consistent UI styling
- 🧹 Clear form fields after save
- 📁 Optional logo display

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x installed
- `Pillow` library for image handling (install using: `pip install pillow`)

### 💻 Run the Application

1. Clone or download this repository.
2. Ensure `logo.png` is in the same folder (optional).
3. Open your terminal or IDE.
4. Run the Python script:

```bash
python contact_book.py
```
---

## 🔐 Login Credentials
- There are no hardcoded usernames or passwords. You may enter any non-empty username and a strong password that - satisfies:
- Minimum 6 characters
- At least 1 letter (A-Z or a-z)
- At least 1 digit (0-9)
- At least 1 special character (e.g., !@#$%^&*)

---

## 🗂 Project Structure
|--Exe.folder            # Exe files <br>
|-- contact_book.py      # Main GUI application<br>
|-- contacts.csv         # Auto-created contact data file<br>
|-- logo.png             # Optional image file for logo<br>
|-- README.md            # Project documentation

---

## 🧠 Concepts Used
- tkinter for GUI creation
- PIL.ImageTk for image rendering
- csv for data storage
- re module for regex validation
- Exception handling and UI feedback using messagebox

---

## 🙋‍♂️ Author
- **CHANDRUPATLA SAI VARUN**
Developed as part of **Techno Hacks Internship** Program