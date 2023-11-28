import numpy as np


def ptk (k,t,p):
    
    if p == '1':
    elif p == '2':
        print("Длины сторон треугольника:")
        p = (p + t + k) / 2
        s = np.sqrt(p * (p - p) * (p - t) * (p - k))
        print("Площадь:", s)
    elif p == '3':
        r = np.sqrt(s/np.pi)
        print("Площадь:", (np.pi * r ** 2))
    else:
        print("Ошибка ввода")

     
