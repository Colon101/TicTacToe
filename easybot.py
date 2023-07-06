from tkinter import *
from tkinter import messagebox
import random

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

def play_random():
    empty_buttons = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]['text'] == ""]
    if empty_buttons:
        row, col = random.choice(empty_buttons)
        buttons[row][col].config(text="⭕")
        buttons[row][col].config(state="disabled")
        if check_winner():
            messagebox.showinfo("⭕", "Player ⭕ Has Won!")
            window.quit()
        else:
            switch_turn()

def play_strategic():
    # Check if the bot can win in the next move
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] == "":
                buttons[i][j].config(text="⭕")
                if check_winner():
                    messagebox.showinfo("⭕", "Player ⭕ Has Won!")
                    window.quit()
                else:
                    buttons[i][j].config(state="disabled")
                    switch_turn()
                    return

    # Check if the player can win in the next move
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] == "":
                buttons[i][j].config(text="❌")
                if check_winner():
                    buttons[i][j].config(text="⭕")
                    buttons[i][j].config(state="disabled")
                    if check_winner():
                        messagebox.showinfo("⭕", "Player ⭕ Has Won!")
                        window.quit()
                    else:
                        switch_turn()
                        return
                else:
                    buttons[i][j].config(text="")
    
    # If no immediate win/defense move is available, play randomly
    play_random()

def button_click(row, col):
    global turn
    if buttons[row][col]['text'] == "":
        buttons[row][col].config(text="❌")
        buttons[row][col].config(state="disabled")
        if check_winner():
            messagebox.showinfo("❌", "Player ❌ Has Won!")
            window.quit()
        else:
            play_strategic()

def switch_turn():
    global turn
    if turn == "X":
        turn = "⭕"
    else:
        turn = "X"

window = Tk()
window.title("Tic-Tac-Toe Easy")

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
