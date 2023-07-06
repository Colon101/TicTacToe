from tkinter import *
from tkinter import messagebox
import os
turn = "X"
def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] and \
           buttons[i][0]['text'] in ["❌", "⭕"]:
            return True
    for i in range(3):
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] and \
           buttons[0][i]['text'] in ["❌", "⭕"]:
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] and \
       buttons[0][0]['text'] in ["❌", "⭕"] or \
       buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] and \
       buttons[0][2]['text'] in ["❌", "⭕"]:
        return True
    return False


def button_click(row, col):
    global turn
    if turn == "X":
        buttons[row][col].config(text="❌")
        turn = "0"
    else:
        turn = "X"
        buttons[row][col].config(text="⭕")
    buttons[row][col].config(state="disabled")
    if check_winner():
        if turn == "X":
            messagebox.showinfo("⭕","Player ⭕ Has Won!")
        else:
            messagebox.showinfo("❌","Player ❌ Has Won!")
            os._exit(1)

window = Tk()
window.title("Tic-Tac-Toe")
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
        buttons[i][j].config(command=lambda row=i, col=j: button_click(row, col))

window.mainloop()