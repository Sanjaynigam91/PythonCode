from array import *

data=array('i',[])

n=int(input("Enter the length of the array: "))

for i in range(n):
    x=int(input("Enter the next value: "))
    data.append(x)

print(data)

num=int(input("Enter the value to search for: "))

k=0

for e in data:
    if e == num:
       print(k)
       break
    k+=1

print(data.index(num))