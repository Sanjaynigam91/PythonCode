import numpy
from numpy import *

data=array([1,2,3,4,5])
print(data)

data1=data+10
print(data1)

data2=data1*100
print(data2)

data3=data2-(data*50)
print(data3)

data4=data3//100
print(data4)

data5=data4%3
print(data5)

data6=numpy.append(data5,100)
print(data6)

data7=numpy.sum(data6)
print(data7)

data8 = numpy.min(data)
print(data8)

data9=numpy.max(data6)
print(data9)

arr=array([1,2,3,4,5])
arr1=array([10,12,13,14,15])

arr3=arr+arr1
print(arr3)

arr4= numpy.concatenate((arr,arr1,arr3))
print(arr4)

arr5=numpy.sort(arr4)
print(arr5)

print(sin(arr1))
print(sin(arr3))
print(sin(arr4))



