a=10

print(id(a))

def gloablandlocal():
     a=9
     x=globals()['a']
     print(id(x))
     print('Inside function',a)
     globals()['a']=16

gloablandlocal()
print('Outside function',a)