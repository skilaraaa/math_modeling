import matplotlib.pyplot as plt 
import numpy as np 
 
def circle_plotter(a = 2, b = 4): 
    x = np.arrange(-2*R, 2*R, 0.1) 
    y = np.arrange(-2*R , 2*R, 0.1) 
 
    X, Y = np.meshgrid(x, y)  
    fxy = y**2/b**2 + y 
  
    plt.contour(X, Y, fxy, levels=[0])  
    plt.savefig('fig_4.png') 
    plt.axis('equal') 
     
if __name__ == '__main__': 
 circle_plotter()