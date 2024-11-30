import random
import tkinter as tk
from tkinter import Label, Button

def roll_dice():
    return random.randint(1, 6)

def on_roll_button_click(result_label):
    result = roll_dice()
    result_label.config(text=f"You rolled: {result}")

def main():
    root = tk.Tk()
    root.title("Dice Rolling Simulator")

    result_label = Label(root, text="Press the Roll button to roll the dice.")
    result_label.pack(pady=20)

    roll_button = Button(
        root, text="Roll", command=lambda: on_roll_button_click(result_label))
    roll_button.pack()

    quit_button = Button(root, text="Quit", command=root.destroy)
    quit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
