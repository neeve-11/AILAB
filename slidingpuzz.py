def next_step(row, col, s):
    board = []
    if row+1 < 3 :
        board.append(swap(row+1, col, row, col, s))
    if col+1 < 3 :
        board.append(swap(row, col+1, row, col, s))
    if row-1 > -1 :
        board.append(swap(row-1, col, row, col, s))
    if col-1 > -1 :
        board.append(swap(row, col-1, row, col, s))
    return board    
        
def swap(row, col, row1, col1, s) :
     k = []
     m = s[row][col]
     n = s[row1][col1]
     i = 0
     j = 0
     for f in s :
         g = []
         for ele in f :
           if i==row and j==col :
               g.append(n)
           elif i==row1 and j==col1 :
               g.append(m)
           else :
               g.append(ele)
           j+=1
         i+=1 
         j=0
         k.append(g)
     return k    
     
def main() :
 target = [[1,2,3], [4,5,6], [7,8,0]]
 moves = 0
 board = [[1,5,2],[4, 8, 0],[7,6,3]]
 #board = [[1,2,3], [4,5,6], [7,0,8]]

 board_generated = [board]
 visited = []

 while board_generated :
    
    check_board = []
    for s in board_generated :
        if s == target :
            num = str(moves)
            print("Total moves ",end='')
            print(num)
            return
        i = 0
        j = 0
        step_board = []
        for row in s :
            for ele in row :
                if ele == 0:
                    step_board.extend(next_step(i, j, s))
                    break
                j+=1
            i+=1
            j=0
        for b in step_board :
            if b not in visited :
                visited.append(b)
                check_board.append(b)
    board_generated = check_board
    moves+=1
 print("Not Possible")
 return
 
main() 