def div(a,b):
    return a/b


def sub(a,b):
    return a-b


def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)

    return inner

div=smart_div(div)
sub=smart_div(sub)
x=int(input("Enter a number:"))
y=int(input("Enter another number:"))
data=div(x,y)
print(data)
data1=sub(x,y)
print(data1)