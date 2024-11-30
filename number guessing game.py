import tkinter as tk
from tkinter import *
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.geometry("750x750")
        self.master.title("Number Guessing Game")

        self.guess = StringVar()
        self.hint = StringVar()
        self.final_score = IntVar()

        Entry(self.master, textvariable=self.guess, width=3, font=('Ubuntu', 50),
              relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)

        Entry(self.master, textvariable=self.hint, width=50, font=('Courier', 15),
              relief=GROOVE, bg='orange').place(relx=0.5, rely=0.7, anchor=CENTER)

        Entry(self.master, textvariable=self.final_score, width=2, font=('Ubuntu', 24),
              relief=GROOVE).place(relx=0.61, rely=0.80, anchor=CENTER)

        Label(self.master, text='I challenge you to guess the number ', font=(
            "Courier", 25)).place(relx=0.5, rely=0.09, anchor=CENTER)

        Label(self.master, text='Score out of 5', font=("Courier", 25)).place(
            relx=0.3, rely=0.80, anchor=CENTER)

        Button(self.master, width=8, text='CHECK', font=('Courier', 25), command=self.check_guess,
               relief=GROOVE, bg='light blue').place(relx=0.5, rely=0.5, anchor=CENTER)

        Button(self.master, width=8, text='NEW GAME', font=('Courier', 10), command=self.new_game,
               relief=GROOVE, bg='light green').place(relx=0.5, rely=0.87, anchor=CENTER)

        self.new_game()  # Start a new game when the application starts

    def generate_random_number(self):
        return random.randint(1, 50)

    def new_game(self):
        self.num = self.generate_random_number()
        self.hint.set("Guess a number between 1 to 50 ")
        self.final_score.set(5)
        self.guess.set("")

    def check_guess(self):
        x = self.guess.get()
        if self.final_score.get() > 0:
            if x == "":
                self.hint.set("Please enter a number.")
            elif not x.isdigit() or not 1 <= int(x) <= 50:
                self.hint.set(
                    "Invalid input. Enter a number between 1 and 50.")
            else:
                self.compare_guess(int(x))
            self.guess.set("")  # Clear the entry box after each check
        else:
            self.hint.set(
                "Game Over, You Lost. The number was {}".format(self.num))

    def compare_guess(self, user_guess):
        if user_guess == self.num:
            self.hint.set("Congratulations, YOU WON!!!")
            self.final_score.set(self.final_score.get() - 1)
        elif user_guess < self.num:
            self.hint.set("Your guess was too low: Guess a higher number")
            self.final_score.set(self.final_score.get() - 1)
        elif user_guess > self.num:
            self.hint.set("Your guess was too High: Guess a lower number")
            self.final_score.set(self.final_score.get() - 1)

if __name__ == "__main__":
    root = tk.Tk()
    NumberGuessingGame(root)
    root.mainloop()
