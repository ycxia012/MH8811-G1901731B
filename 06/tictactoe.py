def TicTacDraw(board):
    """
    Draws a tic-tac-toe board according to input number list.
    0 denotes an O,
    1 denotes an X,
    2 denotes empty cell.
    """
    num_char = {0:"O",1:"X",2:" "}

    n = len(board)
    for i, line in enumerate(board):
        # print out each line element.
        string = ""
        for j, element in enumerate(line):
            string += " {} ".format(num_char[element])
            if j < n-1:
                string += "|"
        print(string)
        # print out the line separator.
        if i < n-1:
            print((4*n-1)*'-')

if __name__ == "__main__":
    example = [[0,1,2],[2,0,0],[1,1,2]]
    TicTacDraw(example)