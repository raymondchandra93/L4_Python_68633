
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

""" main """

def main():
    board = make_board()
    print_board(board)

if __name__ == "__main__":
    main()