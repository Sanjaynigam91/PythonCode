print("Addition")

def add(x,y):
    r=x+y
    return r

a=int(input("enter first number"))
b=int(input("enter second number"))
result=add(a,b)
print(result)

print("Substraction")
def substraction(x,y):
    sub =x-y
    return sub

s1=int(input("enter first number"))
s2=int(input("enter second number"))
subResult=substraction(s1,s2)
print(subResult)
print("Multiplication")
def multiplication(m1,m2):
    mult=m1*m2
    return mult

m=int(input("Enter first number"))
n=int(input("enter second number"))

mulResult=multiplication(m,n)
print(mulResult)
print("Division")
def division(d1,d2):
    div=d1/d2
    return div

num=int(input("enter first number"))
num2=int(input("enter second number"))
divResult=division(num,num2)
print(divResult)