from tkinter import *
from tkinter import messagebox
import random

turn = "X"

def check_winner(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] in ["❌", "⭕"]:
            return True

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] in ["❌", "⭕"]:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in ["❌", "⭕"]:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] in ["❌", "⭕"]:
        return True

    return False

def play_bot_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]

    # Check for winning moves
    for row, col in empty_cells:
        board[row][col] = "⭕"
        if check_winner(board):
            buttons[row][col].config(text="⭕", state="disabled")
            messagebox.showinfo("⭕", "Player ⭕ Has Won!")
            window.quit()
            return
        else:
            board[row][col] = None

    # Check for blocking moves
    for row, col in empty_cells:
        board[row][col] = "❌"
        if check_winner(board):
            board[row][col] = "⭕"
            buttons[row][col].config(text="⭕", state="disabled")
            switch_turn()
            return
        else:
            board[row][col] = None

    # Play random move
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "⭕"
        buttons[row][col].config(text="⭕", state="disabled")
        switch_turn()

def button_click(row, col):
    global turn
    if board[row][col] is None:
        board[row][col] = "❌"
        buttons[row][col].config(text="❌", state="disabled")
        print("Player's move")
        print(board)
        if check_winner(board):
            messagebox.showinfo("❌", "Player ❌ Has Won!")
            window.quit()
        else:
            switch_turn()
            play_bot_move(board)

def switch_turn():
    global turn
    if turn == "X":
        turn = "⭕"
    else:
        turn = "X"

window = Tk()
window.title("Tic-Tac-Toe Medium")

board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

buttons = []

for i in range(3):
    row = []
    for j in range(3):
        button = Button(window, width=10, height=5, command=lambda row=i, col=j: button_click(row, col))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

window.mainloop()
