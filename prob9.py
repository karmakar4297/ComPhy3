import numpy as np
import matplotlib.pyplot as plt
#np.set_printoptions(precision=3, suppress=True)

def f(x):
    if(x<1 and x>-1):
        return 1
    else:
        return 0

xmin =-5
xmax=5
n=128
dx=(xmax-xmin)/(n-1)

sample=np.zeros(n)
xarr=np.zeros(n)

for i in range(n):
    sample[i]=f(xmin+i*dx)
    xarr[i]=xmin+i*dx
nft1=np.fft.fft(sample, norm='ortho')
karr=np.fft.fftfreq(n, d=dx)

nft=nft1*nft1
ift=np.fft.ifft(nft, norm='ortho')



ift=dx*np.sqrt(n)*ift
ift=ift[np.argsort(karr)]

    
plt.plot(xarr, sample, 'g--', label='The box function')
plt.plot(xarr, ift, color='b', label='The convolution with itself')
plt.xlabel('x')
plt.legend()
plt.show()


#In the following, I tried with Zero Padding...
#But I think zero padding is not required here
#Because the sample contain a lot of zeros outside the function region
#Please unomment to check


'''
psample=np.append(sample,np.zeros(n-1))
#print(sample,'\n',psample)

nft1=np.fft.fft(psample, norm='ortho')

nft=nft1*nft1
ift=np.fft.ifft(nft, norm='ortho')


xpoints=np.linspace(xmin,xmax,2*n-1)
delta=xpoints[1]-xpoints[0]
ift=delta*np.sqrt(2*n-1)*ift


ypoints=np.zeros(2*n-1)
for i in range(2*n-1):
    ypoints[i]=f(xpoints[i])
    
plt.plot(xpoints, ypoints, 'g--', label='The box function')
plt.plot(xpoints, ift, color='b', label='The convolution with itself')
plt.title('With zero padding')
plt.legend()
plt.show()
'''


