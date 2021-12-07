over = False
def solve(uniqueLetter, visited, numberValue, ipFirstLetter, res, num1, num2):
     global over 
     if len(uniqueLetter) == len(numberValue) :
         mapper = {}
         for i in range(0,len(uniqueLetter)):
             mapper[uniqueLetter[i]] = numberValue[i]

         if mapper[ipFirstLetter[0]] == 0 or mapper[ipFirstLetter[1]] == 0 or mapper[ipFirstLetter[2]] == 0 :
             return
         f = 0
         for char in res :
             f = f*10+mapper[char]
         n1 = 0    
         for char in num1 :
             n1 = n1*10 +mapper[char]
         n2 = 0
         for char in num2 :
             n2 = n2*10 + mapper[char]

         result = n1 + n2

         if result == f :    
            print("ball = {}".format(n1))
            print("base = {}".format(n2))
            print("games = {}".format(f))
            print(mapper)
            over = True
         return


     for i in range(0, 10) :
          if not visited[i] :
              visited[i]  = True
              numberValue.append(i)
              solve(uniqueLetter, visited, numberValue, ipFirstLetter, res, num1, num2)
              if over == True :
                  return
              visited[i] = False
              numberValue.pop()
     
     return


def main():
   
    num1 = input("enter num1 : ")
    num2 = input("enter num2 : ")
    res = input("enter result : ")

    unique_letter = []
    for char in num1 :
       if char not in unique_letter :
           unique_letter.append(char)
    
    for char in num2 :
        if char not in unique_letter :
            unique_letter.append(char)

    for char in res:
        if char not in unique_letter :
            unique_letter.append(char)


    found = []
    for _ in range(0,10) :
        found.append(False)
    print("RESULT")
    solve(unique_letter, found, [], [num1[0], num2[0], res[0]], res, num1, num2)

if "__main__" == __name__ : 
      main()