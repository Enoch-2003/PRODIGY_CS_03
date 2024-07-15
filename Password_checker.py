import tkinter as tk
from tkinter import messagebox
import re

def assess_password_strength(password):
    length = len(password)
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    strength = 0
    criteria = []

    if length >= 8:
        strength += 1
    else:
        criteria.append("Password should be at least 8 characters long.")

    if has_upper:
        strength += 1
    else:
        criteria.append("Password should include at least one uppercase letter.")

    if has_lower:
        strength += 1
    else:
        criteria.append("Password should include at least one lowercase letter.")

    if has_digit:
        strength += 1
    else:
        criteria.append("Password should include at least one number.")

    if has_special:
        strength += 1
    else:
        criteria.append("Password should include at least one special character.")

    if strength <= 2:
        feedback = "Weak"
    elif strength == 3:
        feedback = "Moderate"
    else:
        feedback = "Strong"

    return feedback, criteria

class PasswordStrengthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Assessor")
        self.root.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter Password:", font=("Helvetica", 14)).pack(pady=20)
        self.password_entry = tk.Entry(self.root, show="*", width=30, font=("Helvetica", 14))
        self.password_entry.pack(pady=10)

        tk.Button(self.root, text="Assess Strength", command=self.assess_password, font=("Helvetica", 12)).pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

        self.criteria_text = tk.Text(self.root, height=5, width=50, font=("Helvetica", 10))
        self.criteria_text.pack(pady=10)

    def assess_password(self):
        password = self.password_entry.get()
        feedback, criteria = assess_password_strength(password)
        self.result_label.config(text=f"Password Strength: {feedback}")

        self.criteria_text.delete(1.0, tk.END)
        if criteria:
            self.criteria_text.insert(tk.END, "\n".join(criteria))
        else:
            self.criteria_text.insert(tk.END, "Your password meets all criteria!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthApp(root)
    root.mainloop()
