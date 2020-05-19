import numpy as np
import csv
import matplotlib.pyplot as plt
#file = open('fft.txt', 'r')

#data=file.readline()


with open('prob2out.txt', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
data=[list(map(float,i)) for i in data]
k=np.zeros(len(data))
ft=np.zeros(len(data))
tft=np.zeros(len(data))
for j in range(len(data)):
    k[j]=data[j][0]
    ft[j]=data[j][1]
    tft[j]=data[j][2]
#print(k)
plt.plot(k,ft,color='b',label='FT using fftw')
plt.plot(k,tft,'g--',label='FT analytically')
plt.title('FT of sinc(x)')
plt.legend()
plt.show()

#####################################################

with open('prob3out.txt', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
data=[list(map(float,i)) for i in data]
k=np.zeros(len(data))
ft=np.zeros(len(data))
tft=np.zeros(len(data))
for j in range(len(data)):
    k[j]=data[j][0]
    ft[j]=data[j][1]
    tft[j]=data[j][2]
#print(k)
plt.plot(k,ft,color='b',label='FT using gsl')
plt.plot(k,tft,'g--',label='FT analytically')
plt.title('FT of sinc(x)')
plt.legend()
plt.show()


###################################################
with open('prob4out.txt', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
data=[list(map(float,i)) for i in data]
k=np.zeros(len(data))
ft=np.zeros(len(data))
tft=np.zeros(len(data))
for j in range(len(data)):
    k[j]=data[j][0]
    ft[j]=data[j][1]
    tft[j]=data[j][2]
#print(k)
plt.plot(k,ft,color='b',label='FT using fftw')
plt.plot(k,tft,'g--',label='FT analytically')
plt.title('FT of Gaussian')
plt.legend()
plt.show()
