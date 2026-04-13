list=[9,11,13,14,17,18]

for i in list:
    if i%5==0:
        print(i)
        break
else:
    print("not found")