import numpy as numpy
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0,10,0.01)
def diff_func(z,t):
    theta,omega = z
    dtheta_dt = omega
    domega_dt = -b * omega - c * np.sin(theta)
    return dtheta_dt, domega_dt
y0 = 0,1
omega0 = 0
z0 = y0,omega0
b = 0.25
c = 5.0
sol = odeint(diff_func, z0, t)
plt.plot(t,sol[:, 1], "b",label = "theta(t)")

plt.legend()
plt.savefig