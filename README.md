

# Tic-Tac-Toe Game with GUI

## Project Overview
This project is a Python-based implementation of the classic Tic-Tac-Toe game with a graphical user interface (GUI) using the tkinter library. It's a simple yet engaging two-player game where players take turns to mark the board with "X" and "O," aiming to achieve three in a row horizontally, vertically, or diagonally.

## How to Run the Game
1. Ensure you have Python installed on your system.
2. Make sure the tkinter library is available (most Python installations come with it).
3. Download or clone the project code from this repository.
4. Run the `tic_tac_toe_gui.py` script using your Python interpreter.
5. The game window will open, and you can start playing by clicking the grid cells.

## Game Rules
- The game is played on a 3x3 grid.
- Two players take turns, one using "X" and the other using "O."
- To win, a player must get three of their symbols in a row, column, or diagonal.
- If all cells are filled, and no player has won, the game ends in a draw.

## Code Structure
- `tic_tac_toe_gui.py` contains the core game logic.
- tkinter is used for creating the graphical user interface.
- The `board` list tracks the game state.
- The `check_win` function determines the game outcome.
- Button clicks are managed by the `on_click` function.
- The main game loop is executed through `root.mainloop()`.

