import random
import nltk
from nltk.corpus import words, wordnet
import tkinter as tk
from tkinter import messagebox, simpledialog

nltk.download('words')
nltk.download('wordnet')

# Load the list of English words
word_list = words.words()

# Function to validate if a word is a valid plural noun
def is_plural(word):
    if not word.endswith('s'):
        return False
    singular = word[:-1]
    return wordnet.synsets(singular, pos=wordnet.NOUN)

class BoggleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Wordle Game")
        self.word_length = 5
        self.solution = None
        self.attempts = 0
        self.max_attempts = 6
        self.hint_used = False
        self.create_widgets()
        self.set_difficulty()

    def create_widgets(self):
        # Instruction label
        self.label = tk.Label(self.master, text="Enter a word:")
        self.label.pack()

        # Container for attempts
        self.attempt_frames = []
        for i in range(self.max_attempts):
            frame = tk.Frame(self.master)
            frame.pack()
            self.attempt_frames.append(frame)

        # Entry box for the user input
        self.entry = tk.Entry(
            self.master, justify="center", font=("Helvetica", 14))
        self.entry.pack()
        self.entry.focus()

        # Submit button
        self.submit_button = tk.Button(
            self.master, text="Submit", command=self.check_guess)
        self.submit_button.pack()

        # Hint button
        self.hint_button = tk.Button(
            self.master, text="Hint", command=self.give_hint)
        self.hint_button.pack()

        # Restart button
        self.restart_button = tk.Button(
            self.master, text="Restart Game", command=self.restart_game)
        self.restart_button.pack()
        self.restart_button.config(state="disabled")

        # Difficulty selection button
        self.difficulty_button = tk.Button(
            self.master, text="Set Difficulty", command=self.set_difficulty)
        self.difficulty_button.pack()

    def set_difficulty(self):
        # Ask the user for the word length
        length = simpledialog.askinteger(
            "Difficulty", "Choose word length (5, 6, or 7):", minvalue=5, maxvalue=7)
        if length:
            self.word_length = length
            self.restart_game()

    def check_guess(self):
        guess = self.entry.get().lower()
        if len(guess) != self.word_length:
            messagebox.showerror(
                "Error", f"Please enter a {self.word_length}-letter word.")
            return
        elif guess not in [word for word in word_list if len(word) == self.word_length] and not is_plural(guess):
            messagebox.showerror("Error", "Not a valid English word.")
            return

        self.display_guess(guess)

        if guess == self.solution:
            messagebox.showinfo("Congratulations!",
                                "You've guessed the word correctly!")
            self.end_game()
        elif self.attempts == self.max_attempts - 1:
            messagebox.showinfo(
                "Game Over", f"You've used all attempts! The word was: {self.solution}")
            self.end_game()
        else:
            self.attempts += 1
            self.entry.delete(0, tk.END)

    def display_guess(self, guess):
        frame = self.attempt_frames[self.attempts]

        for i, char in enumerate(guess):
            label = tk.Label(frame, text=char.upper(), width=4, height=2, font=(
                "Helvetica", 14), relief="solid", bd=1)

            if char == self.solution[i]:
                label.config(bg="green", fg="white")
            elif char in self.solution:
                label.config(bg="yellow", fg="black")
            else:
                label.config(bg="grey", fg="white")

            label.pack(side="left", padx=2, pady=2)

    def give_hint(self):
        if self.hint_used:
            messagebox.showinfo(
                "Hint", "You have already used your hint for this game.")
            return

        # Reveal a random letter in its correct position
        hint_positions = [i for i in range(
            self.word_length) if self.solution[i] not in self.entry.get().lower()]
        if hint_positions:
            hint_index = random.choice(hint_positions)
            hint_letter = self.solution[hint_index].upper()
            messagebox.showinfo(
                "Hint", f"A correct letter is '{hint_letter}' at position {hint_index + 1}.")
            self.hint_used = True
        else:
            messagebox.showinfo("Hint", "No more hints available.")

    def end_game(self):
        self.entry.config(state="disabled")
        self.submit_button.config(state="disabled")
        self.hint_button.config(state="disabled")
        self.restart_button.config(state="normal")

    def restart_game(self):
        global solution
        self.solution = random.choice(
            [word.lower() for word in word_list if len(word) == self.word_length])
        self.attempts = 0
        self.hint_used = False

        for frame in self.attempt_frames:
            for widget in frame.winfo_children():
                widget.destroy()

        self.entry.config(state="normal")
        self.submit_button.config(state="normal")
        self.hint_button.config(state="normal")
        self.restart_button.config(state="disabled")
        self.entry.delete(0, tk.END)
        self.entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    game = BoggleGame(root)
    root.mainloop()
