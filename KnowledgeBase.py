"""
   Knowledge Base buliding

   1.  Tom is cat
   2.  Tom caught a rat
   3.  Tom is owned by John
   4.  Tom is ginger in colour
   5.  Cats like cream
   6.  The cat sat on the mat
   7.  A cat is a mammal
   8.  A bird is an mammal
   9.  Kim is bird   
  10.  bird like river              
  11.  bird is red in colour
  12.  The bird sat on the floor
  13.  Kim caught a fish
  14.  Kim is owned by Neevetha
"""
from kanren import *
from kanren.core import lall

folFacts = var()

tomFeatures = lall(
      #          var   name  caught owner  colour like   5 type sat 
      (eq, (var(), var(), var(), var(), var(), var(), var(), var()), folFacts), 
      (membero,('cat','Tom', var(), var(), var(), var(), var(), var()), folFacts),
      (membero,(var(),'Tom', 'rat', var(), var(), var(), var(), var()), folFacts),
      (membero,(var(),'Tom', var(), 'John', var(), var(), var(), var()), folFacts),
      (membero,(var(),'Tom', var(), var(), 'ginger', var(), var(), var()), folFacts),
      (membero,('cat', var(), var(), var(), var(), 'cream', var(), var()), folFacts),
      (membero,('cat', var(), var(), var(), var(), var(), var(), 'mat'), folFacts),
      (membero,('cat', var(), var(), var(), var(), var(), 'mammal', var()), folFacts),
      (membero,('bird', var(), var(), var(), var(), var(), 'mammal', var()),folFacts),
      (membero,('bird', 'Kim', var(), var(), var(), var(), var(), var()),folFacts),
      (membero,('bird', var(), var(), var(), var(), 'river', var(), var()),folFacts),
      (membero,('bird', var(), var(), var(), 'red', var(), var(), var()), folFacts),
      (membero,('bird', var(), var(), var(), var(), var(), var(), 'floor'), folFacts),
      (membero,(var(), 'Kim', 'fish', var(), var(), var(), var(), var()), folFacts),
      (membero,(var(), 'Kim', var(), 'Neevetha', var(), var(), var(), var()), folFacts)
)

results = run(1, folFacts, tomFeatures)

#print(result)
print()
print("----------Knowledge Base Tuple-----------")
for result in results :
  for r in result :
    if type(r) == tuple :
       print(r)

print()
print("---------Knowledge Base Check------------")
for result in results :
    for r in result :
        if type(r) == tuple :
            print(f"* {r[0]} name is {r[1]}")
            print(f"* {r[1]} owner is {r[3]}")

#print(catName)



