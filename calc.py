import math


def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

def square(x):
    return x**2

def square_root(x):
    return math.sqrt(x)

def even_odd(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")

def primenum(x):
    if x % 2 == 0:
        print("Not Prime")
    else:
        print("Prime")

