from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
 
 
plt.axes(projection = 'polar')
 
rad = np.arange(0, 2 * np.pi, 0.01)
 

for i in rad:
    r = i
    plt.polar(i, r, 'g.')
     


    ani.save('animation_11.gif')