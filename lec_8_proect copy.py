from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
 

fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)
 
def init():
    line.set_data([], [])
    return line,
 
xdata, ydata = [], []
 

def animate(i):
    
    t = 0.1*i  
   
    x = t*np.sin(t)
    y = t*np.cos(t)
      
    xdata.append(x)
    ydata.append(y)
     
    
    line.set_data(xdata, ydata)
     
    return line,
     


plt.axis('off')
 

ani = FuncAnimation(fig, animate, init_func=init,
                               frames=500, interval=20, blit=True)
 
ani.save('animation_13.gif')