import sys
from random import randint 
from collections import Counter


def d(faces):
    return randint(1,faces)

def mydice(): 
    return d(10)-1

#def mydice(): return d(6)

def value(db):
    """
    set dobások (egyforma kockák) értéke darabszám függvényében
    1 -> 1 
    2 -> 3
    3 -> 5
    4 -> 7
    5 -> 9
    """
    return 2*db-1

def kombo(dice, tudás, nehézség):
    "Dob egy kombinációt (melyik számból hány van, érvénytelen kockák nélkül)"
    kockák = (mydice() for _ in range(dice))
    jokockák = filter( lambda x: x<=tudás or x>nehézség, kockák)
    return Counter(jokockák)

def siker(kombok):
    "A kombináció sikeres vagy sem?"
    try:
        return max(kombok.values()) >= 2
    except ValueError:
        return False
    
def sikerertek(kombok):
    "A kombináció numerikus siker értéke"
    if not siker(kombok): return 0
    return sum( map(lambda x: value(x), kombok.values()))

try:
    __, maxtests = sys.argv
    tests = int(maxtests)
except ValueError:
    tests = 10000

def sz(x):
    " % format helper "
    return round(x/tests*100)

print(
"""
---
title: d10 szabályrendszer
geometry: margin=1.5cm
---

""")


print("Sikerszintek (mennyiség) a tudás függvényében")
print("="*40)
print()

maxkocka = 12
maxvalue = 23 

for master in range(10):
    print("Tudásszint:", master)
    print("-"*40)
    print()
    print("n |","|".join(["%3d"%n for n in range(0,maxvalue)]))
    print("--|","|".join(['-'*3]*maxvalue))

    for dicenum in range(1,maxkocka+1):
        probs = Counter()
        probs.update(sikerertek(kombo(dicenum,master,10)) for __ in range(tests))
        print("%2d|"%dicenum,"|".join(["%3d"%sz(probs[k]) for k in range(maxvalue)]))
    
    print()

    
print("Siker esélye kockaszám és tudás szerint")
print("-"*40)
print()

print("n  |","|".join(["%3d"%n for n in range(0,10)]))
print("---|","|".join(['-'*3]*10))

for dicenum in range(1,maxkocka):
    esélyek = []
    for tudás in range(10):
        sikeres= 0
        sikeres = sum([1  for __ in range(tests) if siker(kombo(dicenum,tudás,10))])
        esélyek.append(sikeres)
    print("%3d|"%dicenum,"|".join(["%3d"%sz(s) for s in esélyek]))
