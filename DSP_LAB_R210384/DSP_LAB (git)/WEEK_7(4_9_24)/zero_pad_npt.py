

import numpy as np
import matplotlib.pyplot as plt

def dft(x,N):
    X=[]

    for k in range(N):
        s=0
        for n in range(N):
            s+= x[n]*np.exp(-2j*np.pi*k*n/N)
        X.append(s)
    return np.array(X)

x=np.array([1,2,3,4])

N=len(x)

x1=dft(x,N)

N1=6
N2=9

pad_6 = np.pad(x,(0,N1-N))
pad_9= np.pad(x,(0,N2-N))

X1= dft(pad_6,N1)
X2=dft(pad_9,N2)


plt.subplot(1,3,1)
plt.stem(np.arange(N),np.abs(x1))

plt.subplot(1,3,2)
plt.stem(np.arange(N1),np.abs(X1))

plt.subplot(1,3,3)
plt.stem(np.arange(N2),np.abs(X2))

plt.show()