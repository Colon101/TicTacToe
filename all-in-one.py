from tkinter import *
from tkinter import messagebox
import threading
import random
import math
class TicTacToe:
    def __init__(self, difficulty):
        self.window = Tk()
        self.window.title(f'{difficulty} Tic-Tac-Toe')
        resolution = 300  # Specify the desired resolution
        padding = 50  # Specify the desired padding
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = math.floor((screen_width - resolution) / 2) - padding
        y = math.floor((screen_height - resolution) / 2) - padding
        self.window.geometry(f"{resolution}x{resolution}+{x}+{y}")
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.buttons = []
        self.turn = "X"
        self.difficulty = difficulty

        for i in range(3):
            row = []
            for j in range(3):
                button = Button(self.window, width=10, height=5, command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)
                self.window.grid_columnconfigure(j, weight=1)  # Make columns stretch
            self.buttons.append(row)
            self.window.grid_rowconfigure(i, weight=1)  # Make rows stretch


    def check_winner(self):
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] in ["❌", "⭕"]:
                return True

        # Check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] in ["❌", "⭕"]:
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] in ["❌", "⭕"]:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] in ["❌", "⭕"]:
            return True

        # Check if there are any None values in rows
        for row in self.board:
            if None in row:
                return False

        messagebox.showinfo("Draw!", "Players have made a draw!")
        self.window.quit()
        return False

    def play_bot_move(self):
        if self.difficulty == "Easy":
            self.play_bot_move_easy()
        elif self.difficulty == "Medium":
            self.play_bot_move_medium()
        elif self.difficulty == "Impossible":
            self.play_bot_move_impossible()

    def play_bot_move_easy(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]
        row, col = random.choice(empty_cells)
        self.board[row][col] = "⭕"
        self.buttons[row][col].config(text="⭕", state="disabled")
        self.switch_turn()

    def play_bot_move_medium(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]

        # Check for winning moves
        for row, col in empty_cells:
            self.board[row][col] = "⭕"
            if self.check_winner():
                self.buttons[row][col].config(text="⭕", state="disabled")
                messagebox.showinfo("⭕", "Player ⭕ Has Won!")
                self.window.quit()
                return
            else:
                self.board[row][col] = None

        # Check for blocking moves
        for row, col in empty_cells:
            self.board[row][col] = "❌"
            if self.check_winner():
                self.board[row][col] = "⭕"
                self.buttons[row][col].config(text="⭕", state="disabled")
                self.switch_turn()
                return
            else:
                self.board[row][col] = None

        # Play random move
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = "⭕"
            self.buttons[row][col].config(text="⭕", state="disabled")
            self.switch_turn()

    def play_bot_move_impossible(self):
        best_score = float("-inf")
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    self.board[i][j] = "⭕"
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = None

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            row, col = best_move
            self.board[row][col] = "⭕"
            self.buttons[row][col].config(text="⭕", state="disabled")

            winner = self.check_winner()
            if winner == "⭕":
                messagebox.showinfo("⭕", "Player ⭕ Has Won!")
                self.window.quit()
            elif winner == "draw":
                messagebox.showinfo("Draw!", "Players have made a draw!")
                self.window.quit()

    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner()

        if winner == "⭕":
            return 1
        elif winner == "❌":
            return -1
        elif winner == "draw":
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] is None:
                        board[i][j] = "⭕"
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = None
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] is None:
                        board[i][j] = "❌"
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = None
                        best_score = min(score, best_score)
            return best_score

    def button_click(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = "❌"
            self.buttons[row][col].config(text="❌", state="disabled")
            if self.check_winner():
                messagebox.showinfo("❌", "Player ❌ Has Won!")
                self.window.quit()
            else:
                self.switch_turn()
                self.play_bot_move()

    def switch_turn(self):
        if self.turn == "X":
            self.turn = "⭕"
        else:
            self.turn = "X"

    def start(self):
        self.window.mainloop()

def launch_game(difficulty):
    game = TicTacToe(difficulty)
    game.start()

def launch_medium():
    threading.Thread(target=launch_game, args=("Medium",)).start()

def launch_easy():
    threading.Thread(target=launch_game, args=("Easy",)).start()

def launch_impossible():
    threading.Thread(target=launch_game, args=("Impossible",)).start()

def main_menu():
    window = Tk()
    window.title("Tic Tac Toe - Main Menu")
    resolution = 300  # Specify the desired resolution
    padding = 50  # Specify the desired padding
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = math.floor((screen_width - resolution) / 2) - padding
    y = math.floor((screen_height - resolution) / 2) - padding
    window.geometry(f"{resolution}x{resolution}+{x}+{y}")
    label = Label(window, text="Welcome to Tic Tac Toe", font=("Arial", 20))
    label.pack(pady=20)

    button_medium = Button(window, text="Medium Bot", width=20, height=2, command=launch_medium)
    button_medium.pack(pady=10)

    button_easy = Button(window, text="Easy Bot", width=20, height=2, command=launch_easy)
    button_easy.pack(pady=10)

    button_impossible = Button(window, text="Impossible Bot", width=20, height=2, command=launch_impossible)
    button_impossible.pack(pady=10)

    window.mainloop()

# Launch the main menu
main_menu()
