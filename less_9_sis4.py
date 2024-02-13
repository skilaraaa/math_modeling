import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 
 
x = np.arange(-5,5, 0.01) 

def diff_func(z, x): 
    y,w = z

    dy_dx = w
    dw_dx = np.cos(x) + np.sin(x)
    return dy_dx, dw_dx 
 
x0 = 3
w0 = 0
z0 = x0, w0 
 
sol = odeint(diff_func, z0, x) 
 
plt.plot(x, sol[:, 1], 'b', label='theta(x)') 
plt.legend() 
 
plt.savefig('hg.png')