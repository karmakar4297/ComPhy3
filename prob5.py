import numpy as np
import matplotlib.pyplot as plt
import time

def dft(q,arr):
    wq=0+1j*0
    N=arr.size
    for i in range(N):
        wq=wq+arr[i]*np.exp(-1j*2*np.pi*i*q/N)
    return wq/(np.sqrt(N))
n=4
time_dft=np.zeros(1)
time_fft=np.zeros(1)
narr=np.zeros(1)
while(n<=100):        
    sample=np.arange(n)
    xarr=np.arange(n)
    dft_byhand=np.zeros(n, dtype=np.complex)
    time1=time.time()
    for i in range(n):
        dft_byhand[i]=dft(i, sample)
    time2=time.time()

    dft_numpy=np.fft.fft(sample)
    time3=time.time()

    if(n==4):
        time_dft[0]=time2-time1
        time_fft[0]=time3-time2
        narr[0]=n
    else:
        time_dft=np.append(time_dft,(time2-time1))
        time_fft=np.append(time_fft,(time3-time2))
        narr=np.append(narr,n)
    #print('Time taken without using np.fft = ',(time2-time1))
    #print('Time taken using np.fft = ',(time3-time2))
    n=n+1
plt.plot(narr,time_dft, '.-', color='b', label='Time taken without using numpy.fft')
plt.plot(narr,time_fft, 'g--', label='Time taken using numpy.fft' )
plt.title('DFT method and numpy.fft coparison')
plt.legend()
plt.show()
#print(dft_byhand, dft_numpy)
