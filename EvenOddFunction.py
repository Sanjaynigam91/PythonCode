def count(lst):
    even=0
    odd=0
    for i in lst:
        if i %2==0:
            even+=1
        else:
            odd+=1

    return even,odd

lst=[10,11,12,15,16,20,23,27,30]
even,odd=count(lst)
print("Even :{} and Odd :{}".format(even,odd))