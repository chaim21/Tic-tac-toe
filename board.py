def create_board():
    board = [i for i in range(1,10)]
    return board

def show_board(board):
    print(f'''
    [{board[0]}] | [{board[1]}] | [{board[2]}] 
     ---+----+----
    [{board[3]}] | [{board[4]}] | [{board[5]}] 
     ---+----+----
    [{board[6]}] | [{board[7]}] | [{board[8]}]

''')
