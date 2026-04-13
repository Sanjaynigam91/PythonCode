pos=-1

lst=[1,3,5,7,9,11,13,17,19]

n=int(input("Enter the number:"))

def linear_search(lst,n):

   i=0
   while i<len(lst):
       if lst[i]==n:
           globals()['pos']=i
           return True
       i+=1
   return False



if linear_search(lst,n):
    print("The number is present in the list at position",pos)
else:
    print("The number is not present in the list")