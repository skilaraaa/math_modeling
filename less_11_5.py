import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
t = np.arange(-1, 1, 0.01)
 
 

def diff_func(z,x,y): 
   
   x,z,y = 
    
    dx_dt = 3*x - y + z
    dy_dt = x + y + z
    dz_dt = 4*x - y + 4*z
    return dx_dt, dy_dt,dz_dt
 
 

x = -71
y = 1
z = -3
 

z0 = theta0, omega0
 
k = 0.25
c = 5.0
 
ani.save("gg")