def user_input():
    valid_input = False 
    while not valid_input:
        try:
            num = int(input("enter position:\n"))
            if num < 0 or num > 9:
                print("enter num between 1-9")
            else:
                return num
        except ValueError:
            print("enter num between 1-9")


def is_valid_position(board,symbo):
    valid_position = False 
    while not valid_position:
        position = user_input()
        if board[position-1] == "X" or board[position-1] == "O":
            print("position alredy taken") 
        else:
            return position

