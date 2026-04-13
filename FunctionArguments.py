print("Example of Position Argument")
def add(a,b):
    c=a+b
    return c

result=add(10,20)
print(result)

print("Example of keyword Argument")
def person(name,age):
   print(name,age)

person("Sanjay",30)


print("Example of Default Argument")
def person(name,age=18):
   print(name,age)

person("Sanjay")

print("Example of Variable length Argument")
def addition(*b):
    c=0
    for i in b:
        c+=i
    return c

result=addition(10,20,30,40,50)
print(result)

print("Example of **Kwargs")

def students(name,**data):
    print(name)

    for i,j in data.items():
        print(i,j)

print(students("Sanjay",age=35,city="Lucknow",mob=8433847216))



