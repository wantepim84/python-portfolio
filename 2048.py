import tkinter as tk
import random

class Game2048(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("2048 Game")
        self.geometry("500x500")
        self.resizable(False, False)

        self.grid = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.create_widgets()
        self.start_new_game()
        self.bind("<Key>", self.handle_key)

    def create_widgets(self):
        self.grid_frame = tk.Frame(self)
        self.grid_frame.pack()

        self.score_label = tk.Label(
            self, text=f"Score: {self.score}", font=("Helvetica", 16))
        self.score_label.pack()

        self.cells = [[tk.Label(self.grid_frame, text="", width=4, height=2,
                                font=("Helvetica", 24), bg="#ccc0b3", relief="ridge")
                       for _ in range(4)] for _ in range(4)]

        for i in range(4):
            for j in range(4):
                self.cells[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.restart_button = tk.Button(
            self, text="Restart", command=self.start_new_game, font=("Helvetica", 12))
        self.restart_button.pack(pady=10)

    def add_random_tile(self):
        empty_tiles = [(i, j) for i in range(4)
                       for j in range(4) if self.grid[i][j] == 0]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4

    def update_grid(self):
        for i in range(4):
            for j in range(4):
                value = self.grid[i][j]
                self.cells[i][j].config(
                    text=str(value) if value != 0 else "", bg=self.get_color(value))

        self.score_label.config(text=f"Score: {self.score}")

        if self.check_game_over():
            self.game_over()

    def get_color(self, value):
        colors = {
            0: "#ccc0b3", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
            16: "#f59563", 32: "#f67c5f", 64: "#f67c5f", 128: "#edcf72",
            256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
        }
        return colors.get(value, "#3c3a32")

    def handle_key(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            if event.keysym == "Up":
                self.move_up()
            elif event.keysym == "Down":
                self.move_down()
            elif event.keysym == "Left":
                self.move_left()
            elif event.keysym == "Right":
                self.move_right()
            self.add_random_tile()
            self.update_grid()

    def move_left(self):
        for i in range(4):
            self.merge_row(self.grid[i])

    def move_right(self):
        for i in range(4):
            self.grid[i].reverse()
            self.merge_row(self.grid[i])
            self.grid[i].reverse()

    def move_up(self):
        self.grid = [list(row) for row in zip(*self.grid)]
        self.move_left()
        self.grid = [list(row) for row in zip(*self.grid)]

    def move_down(self):
        self.grid = [list(row) for row in zip(*self.grid)]
        self.move_right()
        self.grid = [list(row) for row in zip(*self.grid)]

    def merge_row(self, row):
        new_row = [num for num in row if num != 0]
        i = 0
        while i < len(new_row) - 1:
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                self.score += new_row[i]
                del new_row[i + 1]
            i += 1
        new_row += [0] * (4 - len(new_row))
        row[:] = new_row

    def check_game_over(self):
        if any(0 in row for row in self.grid):
            return False
        for i in range(4):
            for j in range(4):
                if (j < 3 and self.grid[i][j] == self.grid[i][j + 1]) or (i < 3 and self.grid[i][j] == self.grid[i + 1][j]):
                    return False
        return True

    def game_over(self):
        game_over_label = tk.Label(
            self, text="Game Over!", font=("Helvetica", 24))
        game_over_label.pack()
        self.unbind("<Key>")
        self.restart_button.config(state="normal")

    def start_new_game(self):
        self.grid = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.restart_button.config(state="disabled")

        for i in range(4):
            for j in range(4):
                self.cells[i][j].config(text="", bg="#ccc0b3")

        self.add_random_tile()
        self.add_random_tile()
        self.update_grid()
        self.bind("<Key>", self.handle_key)

if __name__ == "__main__":
    game = Game2048()
    game.mainloop()

