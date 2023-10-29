import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in winning_combinations:
        a, b, c = combo
        if buttons[a]['text'] == buttons[b]['text'] == buttons[c]['text'] != "":
            buttons[a].config(bg='light green')
            buttons[b].config(bg='light green')
            buttons[c].config(bg='light green')
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[a]['text']} wins!")
            root.quit()
            return

    if "" not in [button['text'] for button in buttons]:
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        root.quit()

def on_button_click(i):
    if buttons[i]['text'] == "" and not winner:
        buttons[i]['text'] = player
        buttons[i].config(state='disabled', disabledforeground='black')
        check_winner()
        toggle_player()

def toggle_player():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    label.config(text=f"Player {player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=('normal', 30), height=2, width=5, command=lambda i=i: on_button_click(i)) for i in range(9)]

for i in range(9):
    row, col = divmod(i, 3)
    buttons[i].grid(row=row, column=col)

winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

player = 'X'
winner = None

label = tk.Label(root, text=f"Player {player}'s turn", font=('normal', 14))
label.grid(row=3, columnspan=3)

root.mainloop()
