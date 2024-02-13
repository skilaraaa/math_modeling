import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 
 
x = np.arange(-5, 5, 0.01) 
  
def diff_func(w, x): 
    y, z = w 
 
    dy_dt = y**2 * z 
    dz_dt = z/x - y*z**2 
 
    return dy_dt, dz_dt 
 
y0 = 1  
z0 = -3 
w0 = y0, z0 
 
sol = odeint(diff_func, w0, x) 
 
plt.plot(x, sol[:, 1], 'b', label='theta(x)') 
plt.legend() 
 
plt.savefig('жопа1')