from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
from random import random


def turtle_move(angle_vel, time, alpha0, phi0):
    alpha = angle_vel * np.pi / 180 * time + alpha0
    R = 4 * np.e ** (- 0.1 * alpha)
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    X = x * np.cos(phi0) - y * np.sin(phi0)
    Y = y * np.cos(phi0) + x * np.sin(phi0)
    return X, Y

 
def animate(i):
    for j in range(len(balls)):
        balls[j].set_data(turtle_move(angle_vel=10 , time=i, alpha0=angle[j], phi0=phi[j]))
 

if __name__ == '__main__':
 
    fig, ax = plt.subplots()

    balls = []
    for i in range(100):
        ball, = plt.plot([], [], 'o', color='navy', label='turtle')
        balls.append(ball)

    angle = []
    phi = []
    for i in range(len(balls)):
        angle.append(2 * np.pi * random())
        phi.append(2 * np.pi * random())

 
    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
 
    ani = FuncAnimation(fig,animate,
                        frames=360,
                        interval=30)
 
    ani.save('animation_28.gif')