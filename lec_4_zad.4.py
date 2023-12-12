import numpy as np 
 
def lala(a, b, N): 
    x = np.linspace(a, b, N)  
    y = x**2 
    return y 
a = lala(2, 4,5) 
print(a)