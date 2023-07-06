from tkinter import *

def button_click(row, col):
    buttons[row][col].config(text="X")  # Example: Set the text to X when clicked
    buttons[row][col].config(state="disabled")  # Disable the button after it's clicked

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