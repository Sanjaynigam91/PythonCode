
def greet():
    print("Hello World")
    print("Good Morning")

greet()

print("function with printing result")
def add(a,b):
    c=a+b
    print(c)

add(10,8)

print("function with returning result")

def addition(a,b,c):
    c=a+b+c
    return c

result = addition(10,8,2)
print(result)