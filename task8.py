# Bir funksiyanız olacaq, 
# funksiyada random kitabxanadan istifadə edərək 20 nən 50 arası 5 rəqəm listə append edin.
# Həmən listdəki cüt  rəqəmləri math kitabxanası istifadə edərək kvadrata yüksəldin.

import random
from math import pow

def Numbers():
    i = 0
    mylist = []
    while i<5:
        i += 1
        a = random.randrange(20, 50, 2)
        a = pow(a , 2)
        mylist.append(a)
    return mylist

print(Numbers())
    
        


