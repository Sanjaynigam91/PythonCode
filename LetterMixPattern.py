for i in range(4):
    for j in range(i+1):
        print(chr(65+j) +" ",end="")
    for j in range(4-i-1):
        print(chr(80+j+i) +" ",end="")
    print()    