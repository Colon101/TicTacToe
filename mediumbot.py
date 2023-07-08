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

def play_random(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "⭕"
        buttons[row][col].config(text="⭕", state="disabled")
        if check_winner(board):
            messagebox.showinfo("⭕", "Player ⭕ Has Won!")
            window.quit()
        else:
            switch_turn(board)

def play_strategic(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                # Check if the bot's move allows the player to win in the next move
                board[i][j] = "⭕"
                if check_winner(board):
                    # The player can win, try a different move
                    board[i][j] = None
                    continue
                
                # Reset the bot's move
                board[i][j] = None

                # Simulate bot's move
                board[i][j] = "⭕"

                if check_winner(board):
                    messagebox.showinfo("⭕", "Player ⭕ Has Won!")
                    window.quit()
                else:
                    # Check if opponent can win in the next move
                    for x in range(3):
                        for y in range(3):
                            if board[x][y] is None:
                                # Simulate opponent's move
                                board[x][y] = "❌"
                                if check_winner(board):
                                    # Opponent can win, block their move
                                    board[x][y] = "⭕"
                                    buttons[x][y].config(text="⭕", state="disabled")
                                    switch_turn(board)
                                    return board
                                # Reset opponent's move
                                board[x][y] = None
                    # No winning move for opponent, make the bot's move
                    buttons[i][j].config(text="⭕", state="disabled")
                    switch_turn(board)
                    return

def button_click(row, col, board):
    global turn
    if board[row][col] is None:
        board[row][col] = "❌"
        buttons[row][col].config(text="❌", state="disabled")
        if check_winner(board):
            messagebox.showinfo("❌", "Player ❌ Has Won!")
            window.quit()
            print(board)
        else:
            print("my move")
            print(board)
            board = play_strategic(board)
            print("bot's move")
            print(board)

def switch_turn(board):
    global turn
    if turn == "X":
        turn = "⭕"
    else:
        turn = "X"

window = Tk()
window.title("Tic-Tac-Toe Easy")

board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

buttons = []

for i in range(3):
    row = []
    for j in range(3):
        button = Button(window, width=10, height=5)
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

for i in range(3):
    for j in range(3):
        buttons[i][j].config(command=lambda row=i, col=j: button_click(row, col, board))

window.mainloop()
