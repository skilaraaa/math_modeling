
import numpy as np 
 
def aaa(umnozhoit): 
    a = 1 
    for i in range(len(umnozhoit)): 
        a = a*umnozhoit[i] 
    return a 
b = np.arange(6, 6, 6) 
a(b) 
print(aaa(b))