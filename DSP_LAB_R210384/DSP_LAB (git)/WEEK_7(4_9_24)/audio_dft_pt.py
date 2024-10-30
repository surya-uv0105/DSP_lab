
import numpy as np
import matplotlib.pyplot as plt
import librosa


def dft(x,N):
    X=[]
    for k in range(N):
        s=0
        for n in range(N):
            s+=x[n]*np.exp(-2j*np.pi*k*n)
        
        X.append(s)
    return np.array(X)


x_8000,fs_8000= librosa.load("/home/surya/Downloads/DSP_LAB_R210384/DSP_LAB (git)/WEEK_7(4_9_24)/whisper-trail-2ogg-14429.wav",sr=8000)

x_16000,fs_16000= librosa.load("/home/surya/Downloads/DSP_LAB_R210384/DSP_LAB (git)/WEEK_7(4_9_24)/whisper-trail-2ogg-14429.wav",sr=1600)


#or 
'''
x_8000 = librosa.resample(x, orig_sr=fs, target_sr=8000)
x_1600 = librosa.resample(x, orig_sr=fs, target_sr=1600)
'''
N1=800
N2=1600
x1 = dft(x_8000[:N1],N1)
x2=dft(x_16000[:N2],N2)

plt.subplot(2,1,1)
plt.plot(np.arange(N1),np.abs(x1))



plt.subplot(2,1,2)
plt.plot(np.arange(N2),np.abs(x2))

plt.show()



