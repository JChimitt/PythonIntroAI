import numpy as np

data = np.loadtxt('lab2-data.txt', delimiter='\t')
#print(data)
x = data[ : , 0]
y = data[ : , 1]
#print(x)
#print(y)
averageX = np.average(x)
averageY = np.average(y)


b1 = np.sum((y-averageY)*(x-averageX))/np.sum((x-averageX)**2)
b0 = averageY - b1*averageX
print('b1 =',b1)
print('b0 =',b0)

yPred = b0+b1*x

sst = np.sum((y-averageY)**2)
ssr = np.sum((y-yPred)**2)

r2 = 1-(ssr/sst)

print("r2 =",r2)
