def addition(*b):
    c=0
    for i in b:
        c+=i
    return c

result=addition(1,3,0,7,9)
print(result)