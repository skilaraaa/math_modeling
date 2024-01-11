from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt 
import numpy as np 
 
def log_spiral (radius= 10): 
    phi = np.arange(0, 2*radius, 0.1) 
    r = np.e**(0.1*phi) 
    x = r*np.cos(phi) 
    y= r*np.sin(phi) 
    plt.plot(x,  y, label="my spiral") 
    plt.title('log_spiral') 
    plt.savefig('fig_6.png') 

    
 
 def animate(i):
    ball.set_data(circle_move(R=1.5, angle_vel=1, time=i))
 
 
if __name__ == '__main__':
 
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='c', label='Ball')
 
    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
 
    ani = FuncAnimation(fig,
                        animate,
                        frames=360,
                        interval=30)
 
  
if name == '__main__': 
 log_spiral()