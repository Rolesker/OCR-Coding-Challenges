#. = blank space
#p = pawn
#r = rook
#k = knight
#b = bishop
#q = queen
#K = king
#pieces will have a leading b_ if black, w_ if white, e.g b_k is a black knight
#black pieces should be thought as starting at the bottom (this matters for pawns)
board=[[".",".",".",".",".",".",".","w_K"], #y=0
       ["b_q",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       ["b_K",".",".",".",".",".","b_q","."]] #y=7
#       x=0                         x=7

def set_board():
    board=[[".",".",".",".",".",".",".","w_K"], #y=0
       ["b_q",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       ["b_K",".",".",".",".",".","b_q","."]] #y=7
#       x=0                         x=7

def fill_square(x,y):
    if x<0 or x>7 or y<0 or y>7:
        return False
    if board[y][x]==".":
        board[y][x]="!"
        return True
    return False

def check_square(x,y):
    if x<0 or x>7 or y<0 or y>7:
        return
    if board[y][x]==".":
        return "safe"

def process_pawn(x,y,colour):
    if y==0:
        return
    if colour=="b":
        dir=-1
    else:
        dir=1
        
    if x!=0:
        fill_square(x-1,y+dir)
    if x!=7:
        fill_square(x+1,y+dir)

def process_rook(x,y):
    i=x+1
    while i<8:
        if fill_square(i,y)==False:
            break
        i+=1
    i=x-1
    while i>-1:
        if fill_square(i,y)==False:
            break
        i-=1
    i=y+1
    while y>-1:
        if fill_square(x,i)==False:
            break
        i-=1
    i=y-1
    while y<8:
        if fill_square(x,i)==False:
            break
        i+=1

def process_knight(x,y):
    fill_square(x-2,y+1)
    fill_square(x-2,y-1)
    fill_square(x-1,y+2)
    fill_square(x-1,y-2)
    fill_square(x+1,y-2)
    fill_square(x+1,y+2)
    fill_square(x+2,y+1)
    fill_square(x+2,y-1)


def process_bishop(x,y):
    j=1
    while fill_square(x+j,y-j):
        j+=1
    j=1
    while fill_square(x-j,y-j):
        j+=1
    j=1
    while fill_square(x+j,y+j):
        j+=1
    j=1
    while fill_square(x-j,y+j):
        j+=1
    

def process_queen(x,y):
    process_rook(x,y)
    process_bishop(x,y)

def process_king(x,y):
    fill_square(x-1,y)
    fill_square(x+1,y)
    fill_square(x-1,y-1)
    fill_square(x+1,y-1)
    fill_square(x-1,y+1)
    fill_square(x+1,y+1)
    fill_square(x,y-1)
    fill_square(x,y+1)
    
def check_around_king(x,y): #return true if in danger all around
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if not(j==0 and i==0):
                sq=check_square(x+i,y+j)
                if sq=="safe":
                    return False
    return True

def checkmate_checker(colour,c):
    for i in range(8):
        for j in range(8):
            if not(board[i][j]=="." or board[i][j]=="!"):
                piece=board[i][j].split("_")
                if piece[0]==colour:
                    if piece[1]=="p":
                        process_pawn(j,i,piece[0])
                    elif piece[1]=="r":
                        process_rook(j,i)
                    elif piece[1]=="k":
                        process_knight(j,i)
                    elif piece[1]=="b":
                        process_bishop(j,i)
                    elif piece[1]=="q":
                        process_queen(j,i)
                    elif piece[1]=="K":
                        process_king(j,i)
                    board[i][j]=piece[0]+"_"+piece[1]
                elif piece[1]=="K":
                    enemy_king_coords=[j,i]
    if check_around_king(enemy_king_coords[0],enemy_king_coords[1]):
        print(colour+c+" has sucessfully checkmated the enemy")
    else:
        print(colour+c+" did not achieve a checkmate")

def main():
    checkmate_checker("w","hite")
    print()
    board=[[".",".",".",".",".",".",".","w_K"], #board needs reseting to check both sides
       ["b_q",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".","."],
       ["b_K",".",".",".",".",".","b_q","."]]
    checkmate_checker("b","lack")
    
main()