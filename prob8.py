import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def f(x, y):
    return np.exp(-(x**2+y**2))

xmin=-20.0
xmax=20.0
ymin=-20.0
ymax=20.0
nx=32
ny=32
dx=(xmax-xmin)/(nx-1)
dy=(ymax-ymin)/(ny-1)
sample=np.zeros((nx,ny))
xarr=np.zeros(nx)
yarr=np.zeros(ny)
for i in range(nx):
    for j in range(ny):
        sample[i][j]=f(xmin+i*dx,ymin+j*dy)
        yarr[i]=ymin+j*dy
    xarr[i]=xmin+i*dx
nft=np.fft.fft2(sample, norm='ortho')

kxarr=np.fft.fftfreq(nft.shape[0], d=dx)
kyarr=np.fft.fftfreq(nft.shape[1], d=dy)
kxarr=1*2*np.pi*kxarr
kyarr=1*2*np.pi*kyarr
factor=np.exp(-1j*kxarr*xmin)*np.exp(-1j*kyarr*ymin)
aft=dx*dy*np.sqrt(nx/(2.0*np.pi))*np.sqrt(ny/(2.0*np.pi))*factor*nft
X,Y=np.meshgrid(kxarr, kyarr)
Z=np.abs(aft)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z)
ax.set_xlabel(r'$k_x$')
ax.set_ylabel(r'$k_y$')
ax.set_zlabel(r'$\tildef(k)$')
plt.title('FT of 2-d Gaussian')
plt.show()

