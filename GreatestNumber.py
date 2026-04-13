x=int(input('Enter a number: '))
y=int(input('Enter another number: '))
z=int(input('Enter another number: '))

if x>y and x>z:
    print(f"{x} is greater than {y} and {z}")
elif y>x and y>z:
    print(f"{y} is greater than {x} and{z}")
else:
    print(f"{z} is greater than {x} and {y}")