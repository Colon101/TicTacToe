from tkinter import *
from tkinter import messagebox
import os
PLAYER = "❌"
BOT = "⭕"

def check_winner(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] in [PLAYER, BOT]:
            return board[i][0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] in [PLAYER, BOT]:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in [PLAYER, BOT]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] in [PLAYER, BOT]:
        return board[0][2]

    # Check if there are any empty cells
    for row in board:
        if None in row:
            return None

    # It's a draw
    return "draw"

def play_bot_move(board):
    best_score = float("-inf")
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = BOT
                score = minimax(board, 0, False)
                board[i][j] = None

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    if best_move:
        row, col = best_move
        board[row][col] = BOT
        buttons[row][col].config(text=BOT, state="disabled")

        winner = check_winner(board)
        if winner == BOT:
            messagebox.showinfo(BOT, "Player {} Has Won!".format(BOT))
            window.quit()
        elif winner == "draw":
            messagebox.showinfo("Draw!", "Players have made a draw!")
            window.quit()

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)

    if winner == BOT:
        return 1
    elif winner == PLAYER:
        return -1
    elif winner == "draw":
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = BOT
                    score = minimax(board, depth + 1, False)
                    board[i][j] = None
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = PLAYER
                    score = minimax(board, depth + 1, True)
                    board[i][j] = None
                    best_score = min(score, best_score)
        return best_score

def button_click(row, col):
    if board[row][col] is None:
        board[row][col] = PLAYER
        buttons[row][col].config(text=PLAYER, state="disabled")

        winner = check_winner(board)
        if winner == PLAYER:
            messagebox.showinfo(PLAYER, "Player {} Has Won!".format(PLAYER))
            window.quit()
        elif winner is None:
            play_bot_move(board)

window = Tk()
window.title("Tic-Tac-Toe Unbeatable")

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
