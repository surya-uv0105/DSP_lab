
#doesnot change the sequence , but interpolates

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

N_pad=2*N   #zero pad for double lenght

pad = np.pad(x,(0,N_pad-N))

x2=dft(pad,N_pad)

plt.subplot(1,2,1)
plt.stem(np.arange(N),np.abs(x1))

plt.subplot(1,2,2)
plt.stem(np.arange(N_pad),np.abs(x2))

plt.show()