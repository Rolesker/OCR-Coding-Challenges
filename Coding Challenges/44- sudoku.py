# sudoku boards should use "." as a blank space and be a 2d array

def solve_sudoku(board):
    solved=False
    #used to keep track of which numbers are appearing way (with no repeats)
    rows=[set() for i in range(9)]
    cols=[set() for i in range(9)]
    boxes=[set() for i in range(9)]
    #fill in information based on starting board
    for i in range(9):
        for j in range(9):
            if board[i][j]!=".":
                num=int(board[i][j])
                rows[i].add(num)
                cols[j].add(num)
                box_id=i // 3 * 3 +j // 3 #converts the coordinates to a 0-8 range 
                boxes[box_id].add(num)

    def backTrack(i,j):
        nonlocal solved
        if i==9:
            solved=True
            return
        new_i=i+(j+1)//9 #iterates i whenever j reaches the end of a row
        new_j=(j+1)%9 #increases j with wrapping around if it goes out of the row
        if board[i][j]!=".":
            backTrack(new_i,new_j)
        else:
            for k in range(1,10):
                box_id=i // 3 * 3 + j // 3
                if k not in rows[i] and k not in cols[j] and k not in boxes[box_id]:
                    #assumes that the number k belongs at [i,j] and tries this
                    rows[i].add(k)
                    cols[j].add(k)
                    boxes[box_id].add(k)
                    board[i][j]=str(k)
                    backTrack(new_i,new_j)
                    if not solved: #this will never be reached if the placement was correct
                        rows[i].remove(k)
                        cols[j].remove(k)
                        boxes[box_id].remove(k)
                        board[i][j]="."
    backTrack(0,0)
    return board

print(solve_sudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
    ))