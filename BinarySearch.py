pos=-1
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,45,90,100]

n=int(input("Enter the number:"))
def binary_search(lst,n):
    l=0
    u=len(lst)-1
    while l<=u:
        mid=(l+u)//2
        if lst[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if lst[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False

if binary_search(lst,n):
    print("The number is present in the list at position ",pos+1)
else:
    print("The number is not present in the list")
