#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def print_board(board):
    """
    Function to print the current board state.
    """
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("---------")
    print("\n")

def check_winner(board):
    """
    Function to check if there is a winner.
    Returns 'X' if player X wins, 'O' if player O wins, or None if no winner yet.
    """
    for row in board:
        if all([cell == 'X' for cell in row]):
            return 'X'
        elif all([cell == 'O' for cell in row]):
            return 'O'
    
    for col in range(3):
        if all([board[row][col] == 'X' for row in range(3)]):
            return 'X'
        elif all([board[row][col] == 'O' for row in range(3)]):
            return 'O'
    
    if all([board[i][i] == 'X' for i in range(3)]) or all([board[i][2-i] == 'X' for i in range(3)]):
        return 'X'
    elif all([board[i][i] == 'O' for i in range(3)]) or all([board[i][2-i] == 'O' for i in range(3)]):
        return 'O'
    
    return None

def main():
    board = np.array([[' ' for _ in range(3)] for _ in range(3)])
    player = 'X'
    
    print("Welcome to Tic-Tac-Toe (XOX) Game!")
    print("Player 'X' starts first.")
    print("Enter your move by specifying row and column (e.g., '1,1' for first row and first column).")
    
    while True:
        print_board(board)
        move = input(f"Player '{player}', enter your move (row,col): ")
        
        try:
            row, col = map(int, move.split(','))
            if board[row-1][col-1] != ' ':
                print("Cell already occupied. Try again.")
                continue
            board[row-1][col-1] = player
            
            # Check for winner
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player '{winner}' wins!")
                break
            
            # Check for tie
            if ' ' not in board:
                print_board(board)
                print("It's a tie!")
                break
            
            # Switch player
            player = 'O' if player == 'X' else 'X'
        
        except ValueError:
            print("Invalid input format. Please enter row and column numbers separated by comma.")
        except IndexError:
            print("Invalid move. Row and column numbers must be between 1 and 3.")

if __name__ == "__main__":
    main()


# In[ ]:




