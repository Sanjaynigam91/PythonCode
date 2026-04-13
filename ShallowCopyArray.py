from numpy import *

marks=array([60,70,80,90,95])

marks1=marks.view()

marks[2]=75

print(marks)
print(marks1)
print(log(marks1))
print(tan(marks1))
print(greater(marks,marks1))
print(greater_equal(marks,marks1))
