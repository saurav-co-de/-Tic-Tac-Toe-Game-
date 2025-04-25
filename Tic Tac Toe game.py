# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 12:25:03 2025

@author: Saurav K
"""

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i] + "|" + board[i+1] + "|" + board[i+2])
        if i < 6:
            print("-+-+-")

def check_win(board, player):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def tic_tac_toe():
    board = [" "] * 9
    player1 = "X"
    player2 = "O"
    current_player = player1
    game_over = False

    while not game_over:
        print_board(board)
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move. Try again.")
            continue

        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif " " not in board:
            print_board(board)
            print("It's a tie!")
            game_over = True
        else:
            current_player = player2 if current_player == player1 else player1

tic_tac_toe()