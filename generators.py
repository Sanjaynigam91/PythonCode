def totenSquare():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1

values=totenSquare()
for x in values:
    print(x)