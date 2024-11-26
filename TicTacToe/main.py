
""" Phase 1 """

def make_board():
    board = []
    for i in range(9):
        board.append(" ")
    
    return board

""" Phase 2 """

def print_board(board):
    print("  0   1   2")
    print("0 {} | {} | {} |".format(board[0], board[1], board[2]))
    print(" ------------")
    print("1 {} | {} | {} |".format(board[3], board[4], board[5]))
    print(" ------------")
    print("2 {} | {} | {} |".format(board[6], board[7], board[8]))

""" Phase 3 """

def get_user_input(board, player):
    print(f"Player {player}")
    
    # Getting input for the row number
    row = int(input("Please enter row number: "))
    while(row < 0 or row > 2):
        row = int(input("Please enter a CORRECT row number(0-2): "))

    # Getting input for the column number
    col = int(input("Please enter column number: "))
    while(col < 0 or col > 2):
        col = int(input("Please enter a CORRECT column number(0-2): "))

    index = row * 3 + col
    if(board[index] != " "):
        print("The space has been taken!")
        get_user_input(board, player)
    else:
        if(player == 1):
            board[index] = "x"
        else:
            board[index] = "o"

""" Phase 4 """

def check_three(board, i1, i2, i3):
    if board[i1] != " " and board[i1] == board[i2] and board[i1] == board[i3]:
        return True
    else:
        return False

def check_win(board, player):
    if (check_three(board, 0, 1, 2) or check_three(board, 3, 4, 5) or check_three(board, 6, 7, 8) or 
        check_three(board, 0, 3, 6) or check_three(board, 1, 4, 7) or check_three(board, 2, 5, 8) or
        check_three(board, 0, 4, 8) or check_three(board, 6, 4, 2)):
        
        print_board(board)
        print(f"Player {player} wins!!")

        return False
    else:
        return True

""" Phase  """

def main():
    board = make_board()
    player = 1
    count = 0
    play_game = True

    while play_game:
        print_board(board)
        get_user_input(board, player)
        play_game = check_win(board, player)
        count += 1

        # checking tie condition
        if count > 8:
            play_game = False
            print("Tie Game")
        
        # change the player
        if player == 1: 
            player = 2
        else: 
            player = 1


if __name__ == "__main__":
    main()