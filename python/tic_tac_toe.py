import random

def print_board(board):
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("   |   |   ")

def check_winner(board, player):
    return (
        (board[0] == board[1] == board[2] == player) or
        (board[3] == board[4] == board[5] == player) or
        (board[6] == board[7] == board[8] == player) or
        (board[0] == board[3] == board[6] == player) or
        (board[1] == board[4] == board[7] == player) or
        (board[2] == board[5] == board[8] == player) or
        (board[0] == board[4] == board[8] == player) or
        (board[2] == board[4] == board[6] == player)
    )

def check_draw(board):
    return " " not in board

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_move(board):
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            return move

def tic_tac_toe():
    board = [" "] * 9
    player_symbol = "X"
    computer_symbol = "O"

    print("Welcome to Tic-Tac-Toe!")
    print_board([str(i + 1) for i in range(9)])

    while True:
        # Player's move
        move = player_move(board)
        board[move] = player_symbol
        print_board(board)
        if check_winner(board, player_symbol):
            print("Congratulations! You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        # Computer's move
        print("Computer's move:")
        move = computer_move(board)
        board[move] = computer_symbol
        print_board(board)
        if check_winner(board, computer_symbol):
            print("Sorry, you lose!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

    print("Game Over.")

# Run the game
tic_tac_toe()
