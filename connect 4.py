import tkinter as tk
from tkinter import messagebox

class ConnectFour:
    def __init__(self, master):
        self.master = master
        self.master.title("Connect Four")
        self.canvas = tk.Canvas(master, width=500, height=550)
        self.canvas.pack()

        self.board = [[0] * 7 for _ in range(6)]  # 6 rows, 7 columns
        self.turn = 1  # Player 1 starts

        self.color_var = tk.StringVar(master)
        self.color_var.set("Red")
        self.color_options = ["Red", "Yellow"]
        self.color_menu = tk.OptionMenu(
            master, self.color_var, *self.color_options)
        self.color_menu.pack()

        self.turn_label = tk.Label(
            master, text="Player 1's Turn", font=("Helvetica", 12))
        self.turn_label.pack()

        self.draw_board()

        self.reset_button = tk.Button(
            master, text="Reset", command=self.reset_game)
        self.reset_button.pack()

        self.title_label = tk.Label(
            master, text="Connect Four", font=("Helvetica", 20))
        self.title_label.pack()

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(6):
            for col in range(7):
                color = "white" if self.board[row][col] == 0 else (
                    "red" if self.board[row][col] == 1 else "yellow")
                self.canvas.create_rectangle(
                    col*70, row*70 + 50, (col+1)*70, (row+1)*70 + 50, fill=color, outline="black")
        self.canvas.bind("<Button-1>", self.drop_piece)

    def drop_piece(self, event):
        col = event.x // 70
        for row in range(5, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = self.turn
                self.draw_board()
                if self.check_winner(row, col):
                    winner = "Player 1" if self.turn == 1 else "Player 2"
                    messagebox.showinfo("Winner", f"{winner} wins!")
                    self.canvas.unbind("<Button-1>")
                    return
                self.turn = 1 if self.turn == 2 else 2
                self.update_turn_label()
                return

    def update_turn_label(self):
        player = "Player 1" if self.turn == 1 else "Player 2"
        self.turn_label.config(
        text=f"{player}'s Turn", font=("Helvetica", 14, "bold"))

    def check_winner(self, row, col):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for d in [-1, 1]:
                r, c = row + d * dr, col + d * dc
                while 0 <= r < 6 and 0 <= c < 7 and self.board[r][c] == self.turn:
                    count += 1
                    r, c = r + d * dr, c + d * dc
            if count >= 4:
                return True
        return False

    def reset_game(self):
        self.board = [[0] * 7 for _ in range(6)]
        self.turn = 1
        self.draw_board()
        self.canvas.bind("<Button-1>", self.drop_piece)
        self.update_turn_label()

def main():
    root = tk.Tk()
    connect_four = ConnectFour(root)
    root.mainloop()

if __name__ == "__main__":
    main()
