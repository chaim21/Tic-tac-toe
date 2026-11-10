from board import create_board , show_board 
from validations import is_valid_position
from wins import check_win


def main():
    board = create_board()
    player = "X"
    count = 0
    while count != 9:
        show_board(board)
        print(f"Player {player}, choose a cell (1-9)")
        choose = is_valid_position(board,player)
        board[choose-1] = player
        if check_win(player,board):
            show_board(board)
            print(f"player {player} wins!!")
            break
        else:
            if player == "X":
                player = "O"
            else:
                player = "X"
        count += 1
    if count == 9:
        show_board(board)
        print("Its a draw!")




       

main()