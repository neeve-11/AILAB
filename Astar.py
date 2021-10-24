from queue import PriorityQueue


Graph = {
            'A' : [('B', 2), ('E', 3)],
            'B' : [('C', 1), ('G', 9)],
            'C' : None,
            'E' : [('D', 6)],
            'D' : [('G', 1)],
            'G' : None
        } 
H = {
        'A' : 11,
        'B' : 6,
        'C' : 99,
        'E' : 3,
        'D' : 1,
        'G' : 7
    }
    


def getPath(q, start, end) :
    
    parent = {}
    parent[start] = start
    
    s = None
    
    while not q.empty() :
        s = q.get()
        
        if s[1] == end :
            break
        else :
         if Graph[s[1]] != None :
          for (v, weight) in Graph[s[1]] :
            q.put((s[0]+H[v]+weight, v))
            parent[v] = s[1]
    
    k = s[1]
    res = []
    if k == end :
        while True :
            res.append(k)
            if k == start :
                break
            k = parent[k]
    res.reverse()
    return res


def main():   
   q = PriorityQueue()
   q.put((0, 'A'))
   print(getPath(q, 'A', 'G'))
  
   
if "__main__" == __name__ :
   main() 