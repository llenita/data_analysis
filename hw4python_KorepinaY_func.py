import numpy as np;

def insert_zero(x):
    n=len(x)
    z=np.zeros(2*n-1)
    for i in range(n):
        z[2*i]= x[i]
    return z
    