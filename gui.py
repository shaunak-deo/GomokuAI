import tkinter as tk
import numpy as np
import gomoku as gm
from gomoku import GomokuState
from policies.GomukuAI import Submission
from policies.random import Random

class GomokuGUI:
    def __init__(self, master, board_size, win_size, ai_policy):
        self.master = master
        self.board_size = board_size
        self.win_size = win_size
        self.ai_policy = ai_policy
        self.buttons = [[None for _ in range(board_size)] for _ in range(board_size)]
        self.state = GomokuState.blank(board_size, win_size)
        self.init_board()
        self.init_menu()
        self.status_label = tk.Label(master, text="Your turn", font=("Arial", 12))
        self.status_label.grid(row=board_size + 1, column=0, columnspan=board_size, sticky="ew")
        self.start_over_button = tk.Button(master, text="Start Over", command=self.reset_game)
        self.start_over_button.grid(row=board_size + 2, column=0, columnspan=board_size, sticky="ew")

    def init_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                button = tk.Button(self.master, width=6, height=3, font=("Arial", 14),
                                   command=lambda x=i, y=j: self.on_click(x, y))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_click(self, x, y):
        if self.state.is_game_over() or self.state.board[0, x, y] != 1:
            return  # Ignore click if the game is over or the cell is not empty

        self.make_move(x, y, gm.MAX)
        ai_move = self.ai_policy(self.state)
        if ai_move:
            self.master.after(500, lambda: self.make_move(*ai_move, gm.MIN))

    def make_move(self, x, y, player):
        self.state = self.state.perform((x, y))
        self.buttons[x][y]['text'] = 'X' if player == gm.MAX else 'O'
        if self.state.is_game_over():
            winner = 'Human' if self.state.current_score() > 0 else 'AI'
            self.status_label['text'] = f"Game Over. Winner: {winner}"
            self.disable_buttons()

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button['state'] = 'disabled'

    def reset_game(self):
        self.state = GomokuState.blank(self.board_size, self.win_size)
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.buttons[i][j]['text'] = ""
                self.buttons[i][j]['state'] = 'normal'
        self.status_label['text'] = "Your turn"

    def init_menu(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)
        game_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="New Game", command=self.reset_game)
        game_menu.add_separator()
        game_menu.add_command(label="Play with Random AI", command=lambda: self.change_ai_policy(Random(15, 5)))
        game_menu.add_command(label="Play with Submission AI", command=lambda: self.change_ai_policy(Submission(15, 5)))
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.master.quit)

    def change_ai_policy(self, policy):
        self.ai_policy = policy
        self.reset_game()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Gomoku AI')
    ai_policy = Submission(15, 5)  # This can be changed using the menu
    app = GomokuGUI(root, 15, 5, ai_policy)
    root.mainloop()
