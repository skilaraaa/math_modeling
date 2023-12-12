import matplotlib.pyplot as plt
import numpy as np

def giperbola_plotter ():
    k = 7
    x = np.arange (1,10,0.01)
    y = k/x
    plt.plot(x,  y, color="r", label="my giperbola", marker=">", ms = 5) 
 
    plt.xlabel("Coord: x")#Вызов оси х 
    plt.ylabel("Coord: y") 
    plt.legend() 
    plt.title('giperbola') 
    plt.savefig('fig_5.png')

if __name__ == "__main__":
    giperbola_plotter()