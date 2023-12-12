import numpy as np 
 
def pk(figura, a, r, h, b): 
    if figura == "круг":        
        S = np.pi *(r**2) 
    elif figura == "прямоугольник": 
        S = a*b 
    elif figura == "треугольник": 
        S = 0.5*a*h 
    return S 
a = pk("круг", 4, 8, 1, 1) 
print(a)