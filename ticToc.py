# X - Human
# O - Computer

# 1|2|3
# 4|5|6
# 7|8|9
from copy import deepcopy

board = { 
          1 : ' ', 2 :' ', 3:' ',
          4 : ' ', 5 :' ', 6:' ',
          7 : ' ', 8 :' ', 9:' ' 
        }
        

def printBoard(board) :
    
    j = 1
    for _ in range(0,3):
        for _ in range(0,3):
           print(board[j]+'|', end='')
           j+=1
        print()   
        for _ in range(0,3):
           print("- ", end='')
        print()

def movesPossible(board) :
    moves = []
    for i in range(1,10):
        if board[i] == ' ':
            moves.append(i)
    return moves
    
def min_prune(board, alpha, beta):
    lis = terminal(board)
    if lis[0] == True :
        if lis[1] == None : 
           return 0, None
        elif lis[1] == 'X':   
           return 1, None
        else :
           return -1, None
           
    value = float("inf")
    best = None
    moves = movesPossible(board)
    for position in moves:
        board1 = deepcopy(board)
        board1[position] = 'O'
        maxVal = max_prune(board1, alpha, beta)[0]
        if maxVal < value :
            best = position
            value = maxVal
        beta = min(beta, value)
        if beta <= alpha :
            break
    return value, best
    
def max_prune(board, alpha, beta):
    lis = terminal(board)
    
    if lis[0] == True :
        if lis[1] == None : 
           return 0, None
        elif lis[1] == 'X':   
           return 1, None
        else :
           return -1, None
           
    value = float("-inf")
    best = None
    moves = movesPossible(board)
    for position in moves :
        board1 = deepcopy(board)
        board1[position] = 'O'
        minVal = min_prune(board1, alpha, beta)[0]
        if minVal > value :
            best = position
            value = minVal
        alpha = max(alpha, value)
        if beta <= alpha :
            break
    return value,best
    
def makeMove(toggle, board) :
    if toggle :
        position = max_prune(board, float("-inf"), float("inf"))[1]
        board[position] = 'X'
    else :
        position = min_prune(board, float("-inf"), float("inf"))[1]
        #print("min_prune : "+str(position))
        board[position] = 'O'
        

def terminal(board) :
     if board[1]==board[2]==board[3] and board[3]!=' ' :
         return True, board[1]
     elif board[4]==board[5]==board[6] and board[6]!=' ':
         return True, board[4]
     elif board[7]==board[8]==board[9] and board[8]!=' ':
         return True, board[7]
     elif board[1]==board[4]==board[7] and board[1]!=' ':
         return True, board[1]
     elif board[2]==board[5]==board[8] and board[8]!=' ':
         return True, board[2]
     elif board[3]==board[6]==board[9] and board[3]!=' ':
         return True, board[3]
     elif board[1]==board[5]==board[9] and board[1]!=' ':
         return True, board[5]
     elif board[3]==board[5]==board[7] and board[3]!=' ':
         return True, board[7]
         
     count = 0
     for i in range(1,10) :
         if board[i] == ' ':
             count+=1
     
     if count == 0:
        return True, None
    
     return False,None    


def main() :
   toggle = True
   while True :
     if terminal(board)[0] :
       break
     else :
       if toggle :
           k = int(input("enter the position from 1-9 :\n"))
           board[k] = 'X'
           toggle = False
       else : 
           print("Computer Move")
           makeMove(toggle, board)
           toggle = True
     printBoard(board)
    
   print("Game Over")
   printBoard(board)
           
   
if __name__ == "__main__" :
    main()