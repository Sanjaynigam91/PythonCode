from numpy import *

arr1=array([10,20,30,40,50])
arr2=arr1.copy()

arr1[2]=60
print(arr1)
print(arr2)

City=array(['GKP','LKO','KNP','DEL','MUM'])

Cities=City.copy()

City[3]='BLR'
print(City)
print(Cities)