def employee(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

employee('Sanjay',age=35,mob=8433847216,city='Lucknow',Company='TCS')
