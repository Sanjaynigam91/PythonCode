from numpy import *

m1=matrix([
    [10,15,20],[1,3,5],[11,13,17]
])
m2=matrix([
    [1,5,2],[21,31,51],[101,103,107]
])
print("Addition :-")
m3=m1+m2
print(m3)
print("Subtraction :-")
m4=m1-m2
print(m4)
print("Multiplication :-")
m5=m1*m2
print(m5)
m5=m1*m2
print(m5)
print("Division :-")
m6=m1/m2
print(m6)
m6=m1/m2
print(m6)
print("Transpose of matrix :-")
m7=m1.T
print(m7)
m7=transpose(m1)
print(m1)
print(m7)
print("Get diagonal :-")
m8=m1.diagonal()
print(m8)
print("Get data type of m1 matrix :-")
m9=m1.data
print(m9)
m11=m1.dtype
print(m11)
print("Convert m1 matrix in single dimension :-")
m11=m1.flatten()
print(m11)

arr=array([
            [10,15,20,25,30,35],
            [1,3,5,7,9,12],
            [11,13,17,14,16,18]
    ])

aar1=arr.flatten()
print(aar1)
print("Array to multidimensional matrix")

arr2=arr.reshape(6,3)
print(arr2)

