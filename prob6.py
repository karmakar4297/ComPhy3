import numpy as np
import matplotlib.pyplot as plt

def f(x):
        return 1
xmin=-5
xmax=5
numpoints=16
dx=(xmax-xmin)/(numpoints-1)

sample_data=np.zeros(numpoints)
xarr=np.zeros(numpoints)

for i in range(numpoints):
    sample_data[i]=f(xmin+i*dx)
    xarr[i]=xmin+i*dx

nft=np.fft.fft(sample_data, norm='ortho')

karr=np.fft.fftfreq(numpoints, d=dx)
karr=1*2*np.pi*karr
factor=np.exp(-1j*karr*xmin)

aft=dx*np.sqrt(numpoints/(2.0*np.pi))*factor*nft



order=np.argsort(karr)
karr=karr[order]
aft=aft[order]
fig=plt.figure()
plt.subplot(1,2,1)
plt.plot(xarr,sample_data)
plt.title('The constant function f(x)=1')
plt.grid(True)
plt.subplot(1,2,2)
plt.plot(karr,aft, '.-', color='b')
plt.title('FT of a consstant function')


plt.grid(True)


plt.show()
#print(karr)

