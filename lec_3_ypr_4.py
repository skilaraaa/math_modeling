import numpy as np
N = 2
M = 3
NxM = np.zeros((N,M))
for i in range(N):
    for j in range(M):
        NxM[i,j] = (np.sin(N*(i+1) + M*(j+1)))
for i in range(N):
    for j in range(M):
        if NxM [i,j] < 0:
            NxM [i,j] = 0
print(NxM)