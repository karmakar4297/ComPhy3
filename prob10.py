import numpy as np
import matplotlib.pyplot as plt

file=open('noise.txt','r')

#data=np.zeros(1)
#temp=file.readline()

#temp=float(temp)


data=np.loadtxt('noise.txt', dtype=float)
fig = plt.figure()
plt.plot(data, label='The noise')
plt.legend()
#plt.show()

dft=np.fft.fft(data)
karr=np.fft.fftfreq(data.size, d=1)
#print(karr)

#plt.plot(dft)
karr=karr[np.argsort(karr)]
sdft=dft[np.argsort(karr)]

fig = plt.figure()
plt.plot(sdft, label='The DFT of the noise')
plt.legend()

spectra=abs(sdft)*abs(sdft)/(data.size)

fig = plt.figure()
plt.plot(spectra, label='Spectra')
plt.legend()


bin=10
fig = plt.figure()
plt.hist(spectra,bin, facecolor='blue',label='binned power spectrum')
plt.legend()
plt.show()
    
    
        
