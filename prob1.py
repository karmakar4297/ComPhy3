import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if (x!=0):
        return np.sin(x)/x
    else:
        return 1
    
def analytical(k):
    if((k>-1)and(k<1)):
        return np.sqrt(np.pi/2.0)
    else:
        return 0
    
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

analytic_ft=np.zeros(karr.size)
for i in range(karr.size):
    analytic_ft[i]=analytical(karr[i])

#order=np.zeros(karr.size)
order=np.argsort(karr)
karr=karr[order]
aft=aft[order]
analytic_ft=analytic_ft[order]
plt.plot(karr,aft, '.-', color='b', label='Using np.fft')
plt.plot(karr,analytic_ft, 'g--', label='Analytic' )
plt.title('Fourier transform of sinc(x)')
plt.legend()
plt.show()
#print(karr)

