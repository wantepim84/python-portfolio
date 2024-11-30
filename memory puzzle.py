import tkinter as tk
from tkinter import messagebox
import random

class MemoryPuzzleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory Puzzle Game")

        # Game settings
        self.rows = 4
        self.cols = 4
        self.total_pairs = (self.rows * self.cols) // 2
        self.card_values = [i for i in range(self.total_pairs)] * 2
        random.shuffle(self.card_values)

        # Game state
        self.selected_cards = []
        self.matched_pairs = 0

        # Create buttons
        self.buttons = []
        for i in range(self.rows):
            row_buttons = []
            for j in range(self.cols):
                btn = tk.Button(master, text=" ", width=6, height=3,
                                command=lambda r=i, c=j: self.card_click(r, c))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

        # Reset button
        reset_button = tk.Button(master, text="Reset", command=self.reset_game)
        reset_button.grid(row=self.rows, columnspan=self.cols)

    def card_click(self, row, col):
        # Check if the selected card is already revealed or two cards are already selected
        if self.buttons[row][col]["text"] != " " or len(self.selected_cards) == 2:
            return

        # Reveal the selected card
        value = self.card_values[row * self.cols + col]
        self.buttons[row][col]["text"] = str(value)

        # Store the selected card
        self.selected_cards.append((row, col))

        # Check for a match when two cards are selected
        if len(self.selected_cards) == 2:
            self.master.after(1000, self.check_match)

    def check_match(self):
        row1, col1 = self.selected_cards[0]
        row2, col2 = self.selected_cards[1]

        value1 = self.card_values[row1 * self.cols + col1]
        value2 = self.card_values[row2 * self.cols + col2]

        # Check if the selected cards match
        if value1 == value2:
            messagebox.showinfo("Match", "You found a match!")
            self.matched_pairs += 1
            if self.matched_pairs == self.total_pairs:
                messagebox.showinfo("Congratulations",
                                    "You've matched all pairs!")
                self.reset_game()
        else:
            # Hide the unmatched cards after a short delay
            self.buttons[row1][col1]["text"] = " "
            self.buttons[row2][col2]["text"] = " "

        # Clear the selected cards
        self.selected_cards = []

    def reset_game(self):
        # Reset game state
        self.card_values = [i for i in range(self.total_pairs)] * 2
        random.shuffle(self.card_values)
        self.selected_cards = []
        self.matched_pairs = 0

        # Reset button texts
        for i in range(self.rows):
            for j in range(self.cols):
                self.buttons[i][j]["text"] = " "

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryPuzzleGame(root)
    root.mainloop()
