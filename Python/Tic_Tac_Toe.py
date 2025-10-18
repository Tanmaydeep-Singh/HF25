import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe Game")
        self.root.geometry("350x400")
        self.root.resizable(False, False)
        self.root.config(bg="#2b2b2b")

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.status_label = tk.Label(
            self.root,
            text="Player X's Turn",
            font=("Helvetica", 16, "bold"),
            bg="#2b2b2b",
            fg="#ffffff"
        )
        self.status_label.pack(pady=10)

        self.frame = tk.Frame(self.root, bg="#2b2b2b")
        self.frame.pack()

        self.create_buttons()

        self.reset_button = tk.Button(
            self.root,
            text="Reset Game",
            font=("Helvetica", 14, "bold"),
            bg="#ffcc00",
            fg="#000000",
            command=self.reset_game
        )
        self.reset_button.pack(pady=20)

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(
                self.frame,
                text="",
                font=("Helvetica", 20, "bold"),
                width=5,
                height=2,
                bg="#3c3f41",
                fg="#ffffff",
                activebackground="#4CAF50",
                command=lambda i=i: self.make_move(i)
            )
            button.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                self.status_label.config(text=f"🎉 Player {self.current_player} Wins!", fg="#00ff00")
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif "" not in self.board:
                self.status_label.config(text="It's a Draw!", fg="#ff0000")
                messagebox.showinfo("Game Over", "It's a Draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for cond in win_conditions:
            a, b, c = cond
            if self.board[a] == self.board[b] == self.board[c] != "":
                for i in cond:
                    self.buttons[i].config(bg="#00cc66")
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.status_label.config(text="Player X's Turn", fg="#ffffff")
        for button in self.buttons:
            button.config(text="", bg="#3c3f41")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()