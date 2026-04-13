from numpy import *

data=array([1,2,3,4,5],int)
data1 =array(['Sanjay','Ajay','Arpit'],str)
data2=array([1.4,5.8,-1.9,999.999],float)
print(data)
print(data1)
print(data2)

arr=array([1,2,3,4,5,10],int)
print(arr)

arr1=linspace(1,10,3)
print(arr1)

arr2=logspace(1,40,6)
print('%.4f' %arr2[0])

arr3=arange(1,20,5)
print(arr3)

arr4=zeros([10])
print(arr4)

arr5=ones([10])
print(arr5)