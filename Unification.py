from kanren import Relation as rel 
from kanren import facts as f 
from kanren import run, var

"""
 To define a relation between the terms
"""

parent = rel()

"""
  1. sasi is parent of neeve
  2. sasi is parent of Pava
  3. kumar is parent of neeve
  4. kumar is parent of Pava
  5. sivam is parent of sasi
"""

f(parent, ("sasi", "neeve"),
              ("sasi", "Pava"),
              ("kumar", "neeve"),
              ("kumar", "Pava"),
              ("sivam", "sasi")
)

"""
  Unification example
"""

x = var()
y = var()
print()

print("* sasi's daughter is ", end="")
print(run(0, x, parent("sasi", x)))

print("* sasi's parent is ", end="")
print(run(0, y, parent("sasi", x), parent(y, "sasi")))


print("* kumar is parent of ",end="")
print(run(0, x, parent("kumar", x)))