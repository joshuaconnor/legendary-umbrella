'''
This is designed to solve the Drive'ya'nuts puzzle.
'''
# list of numbers in each piece, in a clockwise rotation, beginning at 1
a = [1,4,3,6,5,2]
b = [1,6,5,4,3,2]
c = [1,6,4,2,5,3]
d = [1,6,2,4,5,3]
e = [1,6,5,3,2,4]
f = [1,4,6,2,3,5]
g = [1,2,3,4,5,6]
# list containing the board, with pieces arranged in initial order
board = [a,b,c,d,e,f,g]
#board = [1,2,3,4,5,6,7]
calcs = 0

def rotate_piece(center_piece, side_piece, position_on_board):
    # function that takes in the center piece, a side page, and index point (i). 
    # function sets first value of side piece equal to value of center piece at 
    # position i, and rearranges subsequent values to effectively "rotate" the piece. 
    side_piece = side_piece[side_piece.index(center_piece[position_on_board]):] + side_piece[:side_piece.index(center_piece[position_on_board])]
    # function returns the rotated side piece as a list
    return side_piece

def rotate_all():
    # function rotates all pieces on board, with exception of center piece. 
    # for loop starts at first outer piece, moving clockwise.
    for index in range(1,7):
        # rotates each piece
        board[index] = rotate_piece(board[0], board[index], index-1)
        calcs =+ 1
        # tests each piece's edge against adjacent piece's edge value
        if all( [board[1][1] == board[6][5],
                    board[1][5] == board[2][1], 
                    board[2][5] == board[3][1],
                    board[3][5] == board[4][1],
                    board[4][5] == board[5][1],
                    board[5][5] == board[6][1] ] ):
            print 'true'
        
        
# rotate_all()





# cycles through each piece as center piece of board
for z in range(7):
    i=1
    ran = 6
    
    # cycles through each piece as primary secondary piece
    for u in range(6):
        for y in range(ran):
            rotate_all()
            print board
            # moves last piece to space denoted by i
            board.insert(i,board.pop())
        i += 1
        ran -= 1
    # sets last piece to first space
    board.insert(0,board.pop())
    
print calcs
    