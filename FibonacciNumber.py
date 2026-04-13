
def fibonacci(n):
    x=0
    y=1
    z=0

    if n<=0:
        print("Invalid number for fibonacci")
    elif n==1:
        print("Fibonacci number is {}".format(x))
    else:
        print(x)
        print(y)
        for i in range(2,n):
            z=x+y
            x=y
            y=z
            print(z)

num=int(input("Enter a number:"))
fibonacci(num)