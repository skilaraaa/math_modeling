import numpy as np 
from lec_3_ypr_1 import g
h = 100
a = np.pi/3
e = np.e
uglB = 30
V = np.sqrt(g*h * (np.tan(uglB))**2) / (2 * (np.cos(a))**2 * (1 - np.tan(uglB)*(np.tan(a))))

print(V)

