from random import randint 
from collections import Counter


def d(faces):
    return randint(1,faces)

tests = 100000



def rule(dice, num_same, obstacle=0):
    "dob és eldönti hogy a dobás sikeres vagy nem"
    throws = [d(10) for _ in range(dice)]
    obstacles = [d(10) for _ in range(obstacle)]
    sets = (Counter(throws) - Counter(obstacles)).values()
    okset = list(filter(lambda k: k>=num_same, sets))
   # print(throws)
   # print(okset)
   # print("---")
    return len(okset)>0

def rule2(dice, num_same, obstacle=0):
    "dob és eldönti hogy a dobás sikeres vagy nem"
    "két set is van"
    throws = [d(10) for _ in range(dice)]
    sets = (Counter(throws)).values()
    okset = list(filter(lambda k: k>=num_same, sets))
   # print(throws)
   # print(okset)
   # print("---")
    return len(okset)>1
    
for k in range(2,15):
    ok = sum( 1 for __ in filter( bool, [rule2(k,2,0) for __ in range(tests) ]))  
    print(k, ": ", round(ok/tests*100,1), "%")

    
