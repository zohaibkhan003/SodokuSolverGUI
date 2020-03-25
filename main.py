Sodukuboard = [
    [0,0,0,0,8,0,0,0,0],
    [8,0,9,0,7,1,0,2,0],
    [4,0,3,5,0,0,0,0,1],
    [0,0,0,1,0,0,0,0,7],
    [0,0,2,0,3,4,0,8,0],
    [7,3,0,0,0,9,0,0,4],
    [9,0,0,0,0,0,7,0,2],
    [0,0,8,2,0,5,0,9,0],
    [1,0,0,0,4,0,3,0,0]
]      

        
def solve(board):
    find = findspotEmpty(board)
    if not find:
        return True
    else:
        row, col = find
    
        row,col = find         
    for i in range(1,10): # goes through all the numbers that can be played
       if check_row(board,i,(row,col)):    # checks all the validity of a move through the 3 restrictions of soduku
           if check_column(board,i,(row,col)):
                if check_box(board,i,(row,col)):
                    board[row][col] = i # once a valid move is found it is placed on the board

                    if solve(board): # follows a recursion formula where if it doesnt fit, move back and try again
                        return True

                    board[row][col] = 0
    return False



def check_row(board,numchosen,position): # checks row
    for i in range(9):
        if board[position[0]][i] == numchosen: # if row has the same number in row
            if position[1] != i:
                return False
    for j in range(9):
        if board[position[0]][j] != numchosen: # if its a new number in the row return true
            if position[1] == j:
                return True

def check_column(board,numchosen,position): # checks column
    for i in range(9):
        if board[i][position[1]] == numchosen: # if column has the same number in column
            if position[0] != i:
                return False
            
    for j in range(9):
        if board[j][position[1]] != numchosen:# if column doesnt have same number, return true
            if position[0] == j:
                return True


def check_box(board,numchosen,position):
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == numchosen:
                if (i,j) != position:
                    return False
          
        return True


def displayBoard(board): 
    i = 0
    for i in range(9): #i iterates with the length of a 9x9 board
        if i == 0: 
            pass
        elif i % 3 == 0: # divides the board after column 3,6,9
            print("- - - - - - - - - - - - - ")
            
        j = 0
        for j in range(9):
            if j == 0:
                pass 
            elif j % 3 == 0: # for every thrid num of a row
                print(" | ", end="") # end doesnt add the new line
                
            if j == 8:  # end of the board 
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def findspotEmpty(board): # finds the position of an empty  position which is denoted by a 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # row, col of the board

    pass


displayBoard(Sodukuboard)
solve(Sodukuboard)
print("                   ")
print("SOLVED SODUKU BOARD")
print("                   ")
displayBoard(Sodukuboard)
