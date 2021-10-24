
result = []

class Nqueen :
    
    def __init__(self, N) :
        self.N = N
        
    """
    To check wheather the generated matrix is valid
    """
    def isValid(self, row, colPlace, answer):
        rowId = len(colPlace)-1
        diff = 0
        for i in range(0, rowId) :
            diff = abs(colPlace[i] - colPlace[rowId])
            if diff == 0 or diff == rowId - i :
                return False
        return True 
    
    """
    Generates the possible possible position of the queen 
    in the board using backtracking
    """
    def solveNqueen(self, row, colPlace, answer):
       if row == self.N :
           k = []
           for i in colPlace :
               m = []
               for g in range(0, self.N):
                   if i == g :
                       m.append("Q")
                   else :
                       m.append("0") 
               k.append(m)           
           result.append(k)
           return
       
       for i in range(0, self.N) :
           colPlace.append(i)
           if self.isValid(row+1, colPlace, answer) :
              self.solveNqueen(row+1, colPlace, answer)
           colPlace.pop(-1)


def main() :    
   n = Nqueen(4)
   n.solveNqueen(0, [], [])
   print("length number of possible position : "+str(len(result)))
   g = 1
   for j in result :
     print(str(g)+" possibility")    
     for i in j :
      print(i)
     g+=1  
   
if "__main__" == __name__ : 
    main()